from ultralytics import YOLO
import cv2
import os

# =========================
# LOAD MODELS
# =========================
detect_model = YOLO(rDFire_Smoke_Detection_Projectrunsdetecttrain4weightsbest.pt)
class_model = YOLO(rDFinalFireClassificationDS2runsclassifytrainweightsbest.pt)

# =========================
# INPUT PATH
# =========================
input_path = rDFire_Smoke_Detection_Projectfire_cctv.mp4   # 🔁 change here

# =========================
# OUTPUT FOLDER
# =========================
output_dir = rDFire_Smoke_Detection_Projectoutputs
os.makedirs(output_dir, exist_ok=True)

# =========================
# FUNCTION DRAW LABEL
# =========================
def draw_label(img, text, x1, y1, color)
    (w, h), _ = cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX, 0.8, 2)

    # Decide position
    y_text = y1 - 10 if y1 - 10  20 else y1 + 30

    # Background rectangle
    cv2.rectangle(img, (x1, y_text - h - 5), (x1 + w, y_text + 5), color, -1)

    # Text
    cv2.putText(img, text, (x1, y_text),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)


# =========================
# IMAGE PROCESSING
# =========================
if input_path.endswith((.jpg, .png, .jpeg))

    img = cv2.imread(input_path)
    results = detect_model(img)

    found = False

    for r in results
        for box in r.boxes
            found = True

            cls = int(box.cls[0])
            label = detect_model.names[cls]

            x1, y1, x2, y2 = map(int, box.xyxy[0])

            if label == fire
                crop = img[y1y2, x1x2]
                cv2.imwrite(crop.jpg, crop)

                cls_result = class_model(crop.jpg)
                fire_type = cls_result[0].names[cls_result[0].probs.top1]

                text = fFire ({fire_type})
                color = (0, 0, 255)

                print(🔥 Fire detected, fire_type)

            elif label == smoke
                text = Smoke
                color = (255, 255, 0)

                print(💨 Smoke detected)

            else
                continue

            cv2.rectangle(img, (x1, y1), (x2, y2), color, 2)
            draw_label(img, text, x1, y1, color)

    if not found
        print(✅ No FireSmoke detected)
        cv2.putText(img, No FireSmoke, (50, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)

    save_path = os.path.join(output_dir, output_image.jpg)
    cv2.imwrite(save_path, img)
    print(f✅ Saved image {save_path})


# =========================
# VIDEO PROCESSING
# =========================
else
    cap = cv2.VideoCapture(input_path)

    width = int(cap.get(3))
    height = int(cap.get(4))
    fps = int(cap.get(cv2.CAP_PROP_FPS))

    output_path = os.path.join(output_dir, output_video.mp4)

    out = cv2.VideoWriter(output_path,
                          cv2.VideoWriter_fourcc('mp4v'),
                          fps, (width, height))

    while True
        ret, frame = cap.read()
        if not ret
            break

        results = detect_model(frame)
        found = False

        for r in results
            for box in r.boxes
                found = True

                cls = int(box.cls[0])
                label = detect_model.names[cls]

                x1, y1, x2, y2 = map(int, box.xyxy[0])

                if label == fire
                    crop = frame[y1y2, x1x2]
                    cv2.imwrite(crop.jpg, crop)

                    cls_result = class_model(crop.jpg)
                    fire_type = cls_result[0].names[cls_result[0].probs.top1]

                    text = fFire ({fire_type})
                    color = (0, 0, 255)

                elif label == smoke
                    text = Smoke
                    color = (255, 255, 0)

                else
                    continue

                cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
                draw_label(frame, text, x1, y1, color)

        if not found
            cv2.putText(frame, No FireSmoke, (50, 50),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)

        out.write(frame)

    cap.release()
    out.release()

    print(f✅ Video saved at {output_path})