from ultralytics import YOLO

# Load model
model = YOLO('yolov5s.pt')
results = model.predict(source='0', show=True)