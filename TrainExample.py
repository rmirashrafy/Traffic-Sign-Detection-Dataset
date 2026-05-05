
!pip install roboflow

from roboflow import Roboflow

rf = Roboflow(api_key="YOUR_API_KEY")
project = rf.workspace("yolo-self-driving-car").project("crosswalk-sign-recognition")
version = project.version(3)
dataset = version.download("yolov8")
