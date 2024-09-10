import torch
import cv2

model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

def detect_people(frame):
    img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    results = model(img_rgb)

    detections = results.pandas().xyxy[0]
    people_detections = detections[detections['name'] == 'person']


    people_count = len(people_detections)

    for _, row in people_detections.iterrows():
        x1, y1, x2, y2 = int(row['xmin']), int(row['ymin']), int(row['xmax']), int(row['ymax'])
        cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 2)

    return people_count, frame        