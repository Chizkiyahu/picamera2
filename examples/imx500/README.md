# Model zoo

## Example files
| Application Name                             | Task                  |
|----------------------------------------------|-----------------------|
| `imx500_classification_demo.py`              | Classification        |
| `imx500_object_detection_demo.py`            | Object Detection      |
| `imx500_segmentation_demo.py`                | Segmentation          |


### Classification Models

| Model              | Dataset  | Input Size | Color Format | Original Model Accuracy (FP32) | On-chip Model Accuracy (Quantized) | Script Call                                                                                                                                         |
|--------------------|----------|------------|--------------|--------------------------------|------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| efficientnet_b0    | ImageNet | 224x224    | RGB          | 73.88                          | 73.77                              | `python imx500_classification_demo.py --model /usr/share/imx500-models/imx500_network_efficientnet_b0.rpk --softmax`                                |
| efficientnet_lite0 | ImageNet | 224x224    | RGB          | 75.28                          | 74.58                              | `python imx500_classification_demo.py --model /usr/share/imx500-models/imx500_network_efficientnet_lite0.rpk --softmax`                             |
| efficientnetv2_b0  | ImageNet | 224x224    | RGB          | 76.42                          | 76.57                              | `python imx500_classification_demo.py --model /usr/share/imx500-models/imx500_network_efficientnetv2_b0.rpk --preserve-aspect-ratio`                |
| efficientnetv2_b1  | ImageNet | 240x240    | RGB          | 76.93                          | 77.01                              | `python imx500_classification_demo.py --model /usr/share/imx500-models/imx500_network_efficientnetv2_b1.rpk --preserve-aspect-ratio --fps 29`       |
| efficientnetv2_b2  | ImageNet | 260x260    | RGB          | 77.94                          | 77.68                              | `python imx500_classification_demo.py --model /usr/share/imx500-models/imx500_network_efficientnetv2_b2.rpk --preserve-aspect-ratio --fps 26`       |
| levit_128s         | ImageNet | 224x224    | RGB          | 58.31                          | 62.35                              | `python imx500_classification_demo.py --model /usr/share/imx500-models/imx500_network_levit_128s.rpk --preserve-aspect-ratio`                       |
| mnasnet1.0         | ImageNet | 224x224    | RGB          | 73.08                          | 73.14                              | `python imx500_classification_demo.py --model /usr/share/imx500-models/imx500_network_mnasnet1.0.rpk --softmax`                                     |
| mobilenet_v2       | ImageNet | 224x224    | RGB          | 74.18                          | 71.65                              | `python imx500_classification_demo.py --model /usr/share/imx500-models/imx500_network_mobilenet_v2.rpk --preserve-aspect-ratio`                     |
| mobilevit_xs       | ImageNet | 256x256    | GBR          | 72.41                          | 72.29                              | `python imx500_classification_demo.py --model /usr/share/imx500-models/imx500_network_mobilevit_xs.rpk --softmax --preserve-aspect-ratio --fps 22`  |
| mobilevit_xxs      | ImageNet | 256x256    | RGB          | 67.40                          | 67.56                              | `python imx500_classification_demo.py --model /usr/share/imx500-models/imx500_network_mobilevit_xxs.rpk --softmax --preserve-aspect-ratio --fps 26` |
| regnetx_002        | ImageNet | 224x224    | RGB          | 68.20                          | 68.31                              | `python imx500_classification_demo.py --model /usr/share/imx500-models/imx500_network_regnetx_002.rpk --softmax`                                    |
| regnety_002        | ImageNet | 224x224    | RGB          | 69.60                          | 69.44                              | `python imx500_classification_demo.py --model /usr/share/imx500-models/imx500_network_regnety_002.rpk --softmax`                                    |
| regnety_004        | ImageNet | 224x224    | RGB          | 73.37                          | 74.98                              | `python imx500_classification_demo.py --model /usr/share/imx500-models/imx500_network_regnety_004.rpk --softmax`                                    |
| resnet18           | ImageNet | 224x224    | RGB          | 68.55                          | 68.62                              | `python imx500_classification_demo.py --model /usr/share/imx500-models/imx500_network_resnet18.rpk --softmax --fps 29`                              |
| shufflenet_v2_x1_5 | ImageNet | 224x224    | RGB          | 72.50                          | 72.18                              | `python imx500_classification_demo.py --model /usr/share/imx500-models/imx500_network_shufflenet_v2_x1_5.rpk`                                       |
| squeezenet1.0      | ImageNet | 224x224    | RGB          | 57.58                          | 57.24                              | `python imx500_classification_demo.py --model /usr/share/imx500-models/imx500_network_squeezenet1.0.rpk`                                            |

### Object Detection Models

| Model                      | Dataset | Input Size | Color Format | Original Model Accuracy (FP32) | On-chip Model Accuracy (Quantized) | Script Call                                                                                                                                         |
|----------------------------|---------|------------|--------------|--------------------------------|------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| efficientdet_lite0         | COCO    | 320x320    | RGB          | 27.29                          | 27.36                              | `python imx500_object_detection_demo.py --model /usr/share/imx500-models/imx500_network_efficientdet_lite0.rpk`                                     |
| efficientdet_lite0_pp      | COCO    | 320x320    | RGB          | 25.18                          | 25.20                              | `python imx500_object_detection_demo.py --model /usr/share/imx500-models/imx500_network_efficientdet_lite0_pp.rpk --bbox-normalization -r --fps 23` |
| nanodet_plus_416x416       | COCO    | 416x416    | GBR          | 33.16                          | 33.26                              | `python imx500_object_detection_demo.py --model /usr/share/imx500-models/imx500_network_nanodet_plus_416x416.rpk --fps 23`                          |
| nanodet_plus_416x416_pp    | COCO    | 416x416    | GBR          | 32.32                          | 32.25                              | `python imx500_object_detection_demo.py --model /usr/share/imx500-models/imx500_network_nanodet_plus_416x416_pp.rpk --ignore-dash-labels --fps 23`  |
| ssd_mobilenetv2_fpnlite_pp | COCO    | 320x320    | RGB          | 21.90                          | 21.95                              | `python imx500_object_detection_demo.py --model /usr/share/imx500-models/imx500_network_ssd_mobilenetv2_fpnlite_pp.rpk --fps 26`                    |

### Segmentation Models

| Model         | Dataset    | Input Size | Color Format | Original Model Accuracy (FP32) | On-chip Model Accuracy (Quantized) | Script Call                                                                                                     |
|---------------|------------|------------|--------------|--------------------------------|------------------------------------|-----------------------------------------------------------------------------------------------------------------|
| deeplabv3plus | PASCAL VOC | 320x320    | RGB          | 72.41                          | 72.41                              | `python imx500_segmentation_demo.py --model /usr/share/imx500-models/imx500_network_deeplabv3plus.rpk --fps 19` |