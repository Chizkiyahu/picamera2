import argparse
import os
import struct

import cv2
import numpy as np

import picamera2.sony_ivs as IVS
from picamera2 import MappedArray, Picamera2

with open("labels.txt", "r") as f:
    LABELS = f.read().split("\n")

parser = argparse.ArgumentParser()
parser.add_argument("--model", type=str, help="Path of the model")

args = parser.parse_args()

MODEL = args.model

last_results = []


class Classification:
    def __init__(self, id, score):
        """Create a Classification object, recording the id and score."""
        self.id = id
        self.score = score


def parse_and_draw_classification_results(request):
    """Analyse the classification results in the output tensor and draw them on the main output image."""
    parse_classification_results(request)
    draw_classification_results(request)


def parse_classification_results(request, stream="main"):
    """Parse the output tensor into a top 3 classification results."""
    output_tensor = request.get_metadata().get("Imx500OutputTensor")
    if output_tensor:
        results = np.array(output_tensor)
        top_indices = np.argpartition(-results, 3)[:3]
        global last_results
        last_results = [Classification(index, results[index]) for index in top_indices]
    request.results = last_results


def draw_classification_results(request, stream="main"):
    """Draw the classification results for this request onto the ISP output."""
    with MappedArray(request, stream) as m:
        for index, result in enumerate(request.results):
            if LABELS is not None:
                if OUTPUT_TENSOR_SIZE == 1000:
                    label = LABELS[result.id + 1]
                else:
                    label = LABELS[result.id]
            else:
                label = result.id
            text = f"{label}: {result.score}"
            cv2.putText(
                m.array,
                text,
                (5, 15 + index * 20),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.5,
                (0, 255, 0),
                1,
            )


# This must be called before instantiation of Picamera2
IVS.set_network_firmware(os.path.abspath(MODEL))

picam2 = Picamera2()
config = picam2.create_preview_configuration(controls={"FrameRate": 30})
picam2.start(config, show_preview=True)

for _ in range(10):
    try:
        input_tensor_info = picam2.capture_metadata()["Imx500InputTensorInfo"]
        network_name, width, height, num_channels = struct.unpack(
            "64sIII", bytes(input_tensor_info)
        )
        network_name = network_name.decode("utf-8").rstrip("\x00")
        break
    except KeyError:
        pass

for _ in range(10):
    try:
        output_tensor_info = picam2.capture_metadata()["Imx500OutputTensorInfo"]
        network_name, *tensor_data_num, num_tensors = struct.unpack(
            "64s16II", bytes(output_tensor_info)
        )
        network_name = network_name.decode("utf-8").rstrip("\x00")
        tensor_data_num = tensor_data_num[:num_tensors]
        break
    except KeyError:
        pass

INPUT_TENSOR_SIZE = (height, width)
OUTPUT_TENSOR_SIZE = tensor_data_num[0]

picam2.pre_callback = parse_and_draw_classification_results

cv2.startWindowThread()
while True:
    try:
        input_tensor = picam2.capture_metadata()["Imx500InputTensor"]
        if INPUT_TENSOR_SIZE != (0, 0):
            cv2.imshow(
                "Input Tensor",
                IVS.input_tensor_image(
                    input_tensor, INPUT_TENSOR_SIZE, (384, 384, 384), (0, 0, 0)
                ),
            )
            cv2.resizeWindow("Input Tensor", *INPUT_TENSOR_SIZE)
    except KeyError:
        pass
