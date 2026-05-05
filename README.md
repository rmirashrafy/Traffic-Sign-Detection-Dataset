
# Traffic Sign Dataset

## Overview

This dataset is designed for object detection tasks in computer vision, especially for autonomous driving applications. It includes multiple traffic signs, road elements, and signal indicators collected from real-world environments under different lighting and weather conditions.

## Dataset Information

- Total Images: ~2000  
- Annotation Format: YOLO (bounding boxes)  
- Classes: 14  

## Classes and Performance

The dataset was tested using Roboflow 3.0 Object Detection model. Below are the per-class mAP@50 results:

| Class Name        | mAP@50 |
|------------------|--------|
| all              | 78.0%  |
| Barred-area      | 87.0%  |
| Cross-walk       | 93.0%  |
| No-Passing-zone  | 89.0%  |
| Parking-zone     | 80.0%  |
| Priority-over    | 95.0%  |
| Stop             | 92.0%  |
| Turn-left        | 69.0%  |
| Turn-right       | 79.0%  |
| car              | 2.0%   |
| downhill         | 100%   |
| go-straight      | 81.0%  |
| green            | 63.0%  |
| red              | 81.0%  |
| uphill           | (not reported) |

## Model Performance (Overall)

- mAP@50: 78.0%  

## Dataset Structure



dataset/
├── train/       # Images and labels
├── valid/       # Validation set
└── test/        # Test set

data.yaml        # YOLO configuration file
README.md



## Usage (YOLOv8 Example)

Install dependencies:



pip install ultralytics



Train the model:

```python
from ultralytics import YOLO

model = YOLO("yolov8n.pt")

model.train(
    data="data.yaml",
    epochs=50,
    imgsz=640
)
````

## Sample Annotation

Add a sample image with bounding boxes here to show annotation quality.

## Roboflow Link

Add your Roboflow dataset link here.

## License

This dataset is licensed under the AGPL-3.0 License.
Make sure to follow the license terms when using or sharing this dataset.

## Tags

computer-vision, object-detection, dataset, yolo, autonomous-vehicles, deep-learning, traffic-signs

## Use Cases

* Autonomous driving systems
* Traffic sign recognition
* Smart traffic monitoring
* Pedestrian and signal detection

## Contributions

Contributions and improvements are welcome.

