
# Traffic Sign Dataset (Turn-Left & Crosswalk)

## Overview

This dataset is designed for object detection tasks in computer vision, especially for autonomous driving applications. It focuses on two common road elements:

- Turn-Left signs  
- Crosswalks  

The data is collected from real-world road environments under different lighting and weather conditions.

## Dataset Information

- Total Images: ~2000  
- Annotation Format: YOLO (bounding boxes)  
- Classes: 2  

### Classes

| Class Name | Description |
|-----------|------------|
| Turn-Left | Traffic signs indicating left turns |
| Crosswalk | Pedestrian crossing areas |

## Model Performance

The dataset was tested using Roboflow 3.0 Object Detection model:

- mAP@50: 78.1%  
- Precision: 76.8%  
- Recall: 71.4%  

## Dataset Structure



dataset/
├── train/       # Images and labels
├── valid/       # Validation set
└── test/        # Test set

data.yaml        # YOLO configuration file
README.md



## Usage (YOLOv8 Example)

Install dependencies:

```

pip install ultralytics

```

Train the model:

```

from ultralytics import YOLO

model = YOLO("yolov8n.pt")

model.train(
data="data.yaml",
epochs=50,
imgsz=640
)

```

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

- Autonomous driving systems  
- Traffic monitoring  
- Pedestrian detection  
