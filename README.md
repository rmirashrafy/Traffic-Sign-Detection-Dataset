This repository hosts a comprehensive dataset and a fine-tuned model for road sign recognition and environment perception. It is specifically designed to support autonomous vehicle navigation by identifying signs, road geometry, and potential hazards.

📊 Dataset Statistics
The dataset is meticulously partitioned to ensure robust model evaluation:

Total Images: 1,799.

Training Set: 1,431 images.

Validation Set: 249 images.

Test Set: 119 images.

Format: Exported in COCO/YOLO formats.

📈 Model Performance
The model, trained using Roboflow 3.0, shows high reliability in critical safety classes:

Overall mAP@50: 78.1%.

Precision: 76.8%.

Top Performing Classes (mAP50):

Downhill: 100%.

Priority-over: 95%.

Cross-walk: 93%.

Stop: 92%.

🛠 Classes Included
The dataset covers 21 classes including:
Barred-area, Cross-walk, No-Passing-zone, Stop, Turn-left, Turn-right, Uphill, Downhill, Traffic Lights (Red/Green), and more.
