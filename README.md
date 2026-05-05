# Traffic Sign Dataset

<img width="1043" height="533" alt="Screenshot from 2026-05-05 18-22-41" src="https://github.com/user-attachments/assets/d5ce84dd-3e12-4ebf-ab9c-d6b693d43498" />



## Dataset Information

### Overview

This dataset is designed for object detection tasks and includes **14 specific traffic signs** used in RoboCup and FiraCup autonomous car competitions.

The images were carefully selected and curated from a pool of approximately **35,000 images**, focusing only on the relevant signs required for the competitions.

In addition to traffic signs, the dataset includes:

* Dolls representing humans
* Cars
* Orange cone obstacles

Some images contain **multiple objects and labels** on a physically simulated road environment.



### Dataset Details

* **Total Images:** ~1800
* **Annotation Format:** YOLO (bounding boxes)
* **Number of Classes:** 14



### Dataset Structure

```
dataset/
├── train/       # Images and labels
├── valid/       # Validation set
└── test/        # Test set

data.yaml
```



### Installation

```
pip install roboflow
```

### Roboflow Project

```
https://app.roboflow.com/yolo-self-driving-car
```

### Download Dataset (Roboflow)

You can download the dataset directly using Roboflow:

```python

from roboflow import Roboflow

rf = Roboflow(api_key="YOUR_API_KEY")
project = rf.workspace("yolo-self-driving-car").project("crosswalk-sign-recognition")
version = project.version(3)
dataset = version.download("yolov8")
```

### Use Cases

* Autonomous driving systems
* Traffic sign recognition
* Smart traffic monitoring
* Pedestrian and signal detection

---

## Trained Model (Test Model) Information

We trained a **simple object detection model** on this dataset using Roboflow.



### Model Details

* Model URL: `crosswalk-sign-recognition/4`
* Checkpoint: COCO
* Model Type: Roboflow 3.0 Object Detection (Fast)



### Performance (mAP@50)

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

* Overall mAP@50: **78.0%**



<img width="1399" height="805" alt="Screenshot from 2026-05-05 22-44-12" src="https://github.com/user-attachments/assets/c540224d-ae2a-4120-ac10-d9a70024104c" />
