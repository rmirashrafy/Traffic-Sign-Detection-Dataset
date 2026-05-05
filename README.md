
# Traffic Sign Dataset

<img width="1043" height="533" alt="Screenshot from 2026-05-05 18-22-41" src="https://github.com/user-attachments/assets/d5ce84dd-3e12-4ebf-ab9c-d6b693d43498" />

### Overview

This dataset is designed for object detection tasks and includes 14 specific signs used in RoboCup and FiraCup autonomous car competitions. The images have been carefully selected and collected from a total of 35,000 pictures, focusing only on the necessary signs defined in the competition.

In addition, the dataset includes dolls representing humans, real humans, cars, and orange cone obstacles on a physically simulated road. Some images contain more than one sign or label.

We also trained a simple model on this dataset using Roboflow, and the model details are provided below.

### Model Information

* Model URL: `crosswalk-sign-recognition/4`
* Checkpoint: COCO
* Model Type: Roboflow 3.0 Object Detection (Fast)

### Dataset Information

* Total Images: ~1800
* Annotation Format: YOLO (bounding boxes)
* Classes: 14

### Classes and Performance

The dataset was tested using the Roboflow 3.0 Object Detection model. Below are the per-class mAP@50 results:

| Class Name      | mAP@50         |
| --------------- | -------------- |
| all             | 78.0%          |
| Barred-area     | 87.0%          |
| Cross-walk      | 93.0%          |
| No-Passing-zone | 89.0%          |
| Parking-zone    | 80.0%          |
| Priority-over   | 95.0%          |
| Stop            | 92.0%          |
| Turn-left       | 69.0%          |
| Turn-right      | 79.0%          |
| car             | 2.0%           |
| downhill        | 100%           |
| go-straight     | 81.0%          |
| green           | 63.0%          |
| red             | 81.0%          |
| uphill          | (not reported) |

* Overall mAP@50: 78.0%

<img width="1399" height="805" alt="Screenshot from 2026-05-05 22-44-12" src="https://github.com/user-attachments/assets/c540224d-ae2a-4120-ac10-d9a70024104c" />


### Dataset Structure

```
dataset/
├── train/       # Images and labels
├── valid/       # Validation set
└── test/        # Test set

data.yaml
```


Install dependencies:

```
pip install ultralytics
pip install roboflow
```


### Roboflow Link

```
https://app.roboflow.com/yolo-self-driving-car
```

### Use Cases

* Autonomous driving systems
* Traffic sign recognition
* Smart traffic monitoring
* Pedestrian and signal detection
