# --normal code

# from ultralytics import YOLO
# import cv2
# import os

# # =========================
# # LOAD MODELS
# # =========================
# detect_model = YOLO(r"D:\Fire_Smoke_Detection_Project\runs\detect\train4\weights\best.pt")
# class_model = YOLO(r"D:\FinalFireClassificationDS2\runs\classify\train\weights\best.pt")

# # =========================
# # INPUT PATH
# # =========================
# input_path = r"D:\Fire_Smoke_Detection_Project\test2.jpg"

# # =========================
# # OUTPUT FOLDER
# # =========================
# output_dir = r"D:\Fire_Smoke_Detection_Project\outputs"
# os.makedirs(output_dir, exist_ok=True)

# # =========================
# # FUNCTION: DRAW LABEL
# # =========================
# def draw_label(img, text, x1, y1, color):
#     (w, h), _ = cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX, 0.8, 2)

#     y_text = y1 - 10 if y1 - 10 > 20 else y1 + 30

#     cv2.rectangle(img, (x1, y_text - h - 5), (x1 + w, y_text + 5), color, -1)
#     cv2.putText(img, text, (x1, y_text),
#                 cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)


# # =========================
# # IMAGE PROCESSING
# # =========================
# if input_path.endswith((".jpg", ".png", ".jpeg")):

#     img = cv2.imread(input_path)
#     results = detect_model(img)

#     found = False

#     for r in results:
#         for box in r.boxes:
#             found = True

#             cls = int(box.cls[0])
#             label = detect_model.names[cls]

#             x1, y1, x2, y2 = map(int, box.xyxy[0])

#             if label == "fire":
#                 crop = img[y1:y2, x1:x2]
#                 cv2.imwrite("crop.jpg", crop)

#                 cls_result = class_model("crop.jpg")
#                 fire_type = cls_result[0].names[cls_result[0].probs.top1]

#                 text = f"Fire ({fire_type})"
#                 color = (0, 0, 255)

#                 print("🔥 Fire detected:", fire_type)

#             elif label == "smoke":
#                 text = "Smoke"
#                 color = (255, 255, 0)

#                 print("💨 Smoke detected")

#             else:
#                 continue

#             cv2.rectangle(img, (x1, y1), (x2, y2), color, 2)
#             draw_label(img, text, x1, y1, color)

#     if not found:
#         print("✅ No Fire/Smoke detected")
#         cv2.putText(img, "No Fire/Smoke", (50, 50),
#                     cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)

#     save_path = os.path.join(output_dir, "output_image.jpg")
#     cv2.imwrite(save_path, img)
#     print(f"✅ Saved image: {save_path}")


# # =========================
# # VIDEO PROCESSING (OPTIMIZED)
# # =========================
# else:
#     cap = cv2.VideoCapture(input_path)

#     width = int(cap.get(3))
#     height = int(cap.get(4))
#     fps = int(cap.get(cv2.CAP_PROP_FPS))

#     output_path = os.path.join(output_dir, "output_video.mp4")

#     out = cv2.VideoWriter(output_path,
#                           cv2.VideoWriter_fourcc(*'mp4v'),
#                           fps, (width, height))

#     frame_count = 0

#     while True:
#         ret, frame = cap.read()
#         if not ret:
#             break

#         frame_count += 1

#         # 🔥 SKIP FRAMES (2x speed)
#         if frame_count % 2 != 0:
#             continue

#         # 🔥 RESIZE FRAME (faster inference)
#         frame = cv2.resize(frame, (640, 360))

#         results = detect_model(frame)
#         found = False

#         for r in results:
#             for box in r.boxes:
#                 cls = int(box.cls[0])
#                 label = detect_model.names[cls]

#                 x1, y1, x2, y2 = map(int, box.xyxy[0])

#                 # 🔥 Skip very small detections (noise removal)
#                 if (x2 - x1) * (y2 - y1) < 2000:
#                     continue

#                 found = True

#                 if label == "fire":
#                     crop = frame[y1:y2, x1:x2]
#                     cv2.imwrite("crop.jpg", crop)

#                     cls_result = class_model("crop.jpg")
#                     fire_type = cls_result[0].names[cls_result[0].probs.top1]

#                     text = f"Fire ({fire_type})"
#                     color = (0, 0, 255)

#                 elif label == "smoke":
#                     text = "Smoke"
#                     color = (255, 255, 0)

#                 else:
#                     continue

#                 cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
#                 draw_label(frame, text, x1, y1, color)

#         if not found:
#             cv2.putText(frame, "No Fire/Smoke", (50, 50),
#                         cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)

#         out.write(frame)

#     cap.release()
#     out.release()

#     print(f"✅ Optimized video saved at: {output_path}")









# ---optimized


# from ultralytics import YOLO
# import cv2
# import os

# # =========================
# # LOAD MODELS
# # =========================
# detect_model = YOLO(r"D:\Fire_Smoke_Detection_Project\runs\detect\train4\weights\best.pt")
# class_model = YOLO(r"D:\FinalFireClassificationDS2\runs\classify\train\weights\best.pt")

# # =========================
# # INPUT PATH
# # =========================
# input_path = r"D:\Fire_Smoke_Detection_Project\test2.jpg"

# # =========================
# # OUTPUT FOLDER
# # =========================
# output_dir = r"D:\Fire_Smoke_Detection_Project\outputs"
# os.makedirs(output_dir, exist_ok=True)

# # =========================
# # FUNCTION: DRAW LABEL
# # =========================
# def draw_label(img, text, x1, y1, color):
#     (w, h), _ = cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX, 0.8, 2)
#     y_text = y1 - 10 if y1 - 10 > 20 else y1 + 30

#     cv2.rectangle(img, (x1, y_text - h - 5), (x1 + w, y_text + 5), color, -1)
#     cv2.putText(img, text, (x1, y_text),
#                 cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)

# # =========================
# # GET OUTPUT NAME
# # =========================
# filename = os.path.basename(input_path)
# name, ext = os.path.splitext(filename)

# # =========================
# # IMAGE PROCESSING
# # =========================
# if input_path.endswith((".jpg", ".png", ".jpeg")):

#     img = cv2.imread(input_path)
#     results = detect_model(img, conf=0.25)

#     found = False

#     for r in results:
#         for box in r.boxes:
#             cls = int(box.cls[0])
#             label = detect_model.names[cls]

#             x1, y1, x2, y2 = map(int, box.xyxy[0])
#             conf = float(box.conf[0])

#             found = True

#             if label == "fire":
#                 crop = img[y1:y2, x1:x2]
#                 cv2.imwrite("crop.jpg", crop)

#                 cls_result = class_model("crop.jpg")
#                 fire_type = cls_result[0].names[cls_result[0].probs.top1]

#                 text = f"Fire ({fire_type}) {conf:.2f}"
#                 color = (0, 0, 255)  # RED

#             elif label == "smoke":
#                 text = f"Smoke {conf:.2f}"
#                 color = (255, 0, 0)  # 🔥 BRIGHT BLUE (VISIBLE)

#             else:
#                 continue

#             # 🔥 thicker box
#             cv2.rectangle(img, (x1, y1), (x2, y2), color, 3)
#             draw_label(img, text, x1, y1, color)

#     if not found:
#         cv2.putText(img, "No Fire/Smoke", (50, 50),
#                     cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)

#     save_path = os.path.join(output_dir, f"{name}_output{ext}")
#     cv2.imwrite(save_path, img)
#     print(f"✅ Saved image: {save_path}")


# # =========================
# # VIDEO PROCESSING
# # =========================
# else:
#     cap = cv2.VideoCapture(input_path)

#     width = int(cap.get(3))
#     height = int(cap.get(4))
#     fps = int(cap.get(cv2.CAP_PROP_FPS))

#     output_path = os.path.join(output_dir, f"{name}_output.mp4")

#     out = cv2.VideoWriter(output_path,
#                           cv2.VideoWriter_fourcc(*'mp4v'),
#                           fps, (width, height))

#     frame_count = 0

#     while True:
#         ret, frame = cap.read()
#         if not ret:
#             break

#         frame_count += 1

#         if frame_count % 2 != 0:
#             continue

#         frame = cv2.resize(frame, (640, 360))
#         results = detect_model(frame, conf=0.25)

#         found = False

#         for r in results:
#             for box in r.boxes:
#                 cls = int(box.cls[0])
#                 label = detect_model.names[cls]

#                 x1, y1, x2, y2 = map(int, box.xyxy[0])
#                 conf = float(box.conf[0])

#                 if label == "fire" and (x2 - x1) * (y2 - y1) < 2000:
#                     continue

#                 found = True

#                 if label == "fire":
#                     crop = frame[y1:y2, x1:x2]
#                     cv2.imwrite("crop.jpg", crop)

#                     cls_result = class_model("crop.jpg")
#                     fire_type = cls_result[0].names[cls_result[0].probs.top1]

#                     text = f"Fire ({fire_type}) {conf:.2f}"
#                     color = (0, 0, 255)

#                 elif label == "smoke":
#                     text = f"Smoke {conf:.2f}"
#                     color = (255, 0, 0)  # BLUE

#                 else:
#                     continue

#                 cv2.rectangle(frame, (x1, y1), (x2, y2), color, 3)
#                 draw_label(frame, text, x1, y1, color)

#         if not found:
#             cv2.putText(frame, "No Fire/Smoke", (50, 50),
#                         cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)

#         out.write(frame)

#     cap.release()
#     out.release()

#     print(f"✅ Saved video: {output_path}")






# ---optimized with the bounded boxes and confidence scores


from ultralytics import YOLO
import cv2
import os

# =========================
# LOAD MODELS
# =========================
detect_model = YOLO(r"D:\Fire_Smoke_Detection_Project\runs\detect\train4\weights\best.pt")
class_model = YOLO(r"D:\FinalFireClassificationDS2\runs\classify\train\weights\best.pt")

# =========================
# INPUT PATH
# =========================
input_path = r"D:\Fire_Smoke_Detection_Project\metal.jpg"

# =========================
# OUTPUT FOLDER
# =========================
output_dir = r"D:\Fire_Smoke_Detection_Project\outputs"
os.makedirs(output_dir, exist_ok=True)

filename = os.path.basename(input_path)
name, ext = os.path.splitext(filename)

# =========================
# DRAW LABEL
# =========================
def draw_label(img, text, x1, y1, x2, y2, color):
    font_scale = max(0.5, img.shape[1] / 1200)  # adaptive font
    thickness = 2

    (w, h), _ = cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX, font_scale, thickness)

    # ALWAYS SAFE POSITION
    if y1 - 20 > h:
        y_text = y1 - 10
    else:
        y_text = y2 + h + 10

    # Clamp inside image
    y_text = min(y_text, img.shape[0] - 10)

    cv2.rectangle(img, (x1, y_text - h - 5), (x1 + w, y_text + 5), color, -1)

    cv2.putText(img, text, (x1, y_text),
                cv2.FONT_HERSHEY_SIMPLEX,
                font_scale,
                (255, 255, 255),
                thickness)


# =========================
# SAFE CLASSIFICATION
# =========================
def classify_fire(crop):
    try:
        if crop is None or crop.size == 0:
            return "Unknown"

        crop = cv2.resize(crop, (224, 224))  # 🔥 FIX
        result = class_model(crop)

        if result[0].probs is not None:
            cls_id = result[0].probs.top1
            return result[0].names[cls_id]
        else:
            return "Unknown"
    except:
        return "Unknown"


# =========================
# IMAGE
# =========================
if input_path.lower().endswith((".jpg", ".png", ".jpeg")):

    img = cv2.imread(input_path)
    results = detect_model(img, conf=0.25)

    found = False

    all_boxes = []
    for r in results:
        for box in r.boxes:
            all_boxes.append(box)

    # Draw smoke first, fire last
    all_boxes = sorted(all_boxes, key=lambda b: int(b.cls[0]))

    for box in all_boxes:
        cls = int(box.cls[0])
        label = detect_model.names[cls]

        x1, y1, x2, y2 = map(int, box.xyxy[0])
        conf = float(box.conf[0])

        found = True

        if label == "fire":
            crop = img[y1:y2, x1:x2]

            fire_type = classify_fire(crop)

            text = f"Fire ({fire_type}) {conf:.2f}"
            color = (0, 0, 255)

            print(f"🔥 Fire detected: {fire_type} ({conf:.2f})")

        elif label == "smoke":
            text = f"Smoke {conf:.2f}"
            color = (255, 0, 0)

            print(f"💨 Smoke detected ({conf:.2f})")

        else:
            continue

        cv2.rectangle(img, (x1, y1), (x2, y2), color, 3)
        draw_label(img, text, x1, y1, x2, y2, color)

    if not found:
        print("✅ No Fire/Smoke detected")
        cv2.putText(img, "No Fire/Smoke", (50, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)

    save_path = os.path.join(output_dir, f"{name}_output{ext}")
    cv2.imwrite(save_path, img)

    print(f"✅ Saved image: {save_path}")