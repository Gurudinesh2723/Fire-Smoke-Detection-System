from ultralytics import YOLO

# dataset path
data = "dataset/data.yaml"

# -------- YOLOv10 --------
print("Starting YOLOv10 Training...")

model10 = YOLO("yolov10s.pt")

model10.train(
    data=data,
    epochs=50,
    imgsz=512,
    batch=4,
    workers=0,
    device=0,
    project="runs/detect",
    name="yolov10"
)

print("YOLOv10 Training Finished")


# -------- YOLOv11 --------
print("Starting YOLOv11 Training...")

model11 = YOLO("yolov11s.pt")

model11.train(
    data=data,
    epochs=50,
    imgsz=512,
    batch=4,
    workers=0,
    device=0,
    project="runs/detect",
    name="yolov11"
)

print("YOLOv11 Training Finished")