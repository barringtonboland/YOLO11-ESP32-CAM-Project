import cv2
from ultralytics import YOLO

model = YOLO("yolo11n.pt")

source = ' '
cap = cv2.VideoCapture(source)

while cap.isOpened():
    success, frame = cap.read()
    
    if success:
        results = model.predict(frame)

        annotated_frame = results[0].plot()

        cv2.imshow("YOLO Inference", annotated_frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()
