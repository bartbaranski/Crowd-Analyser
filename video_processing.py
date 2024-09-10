import cv2

def process_video(file_path):
    video = cv2.VideoCapture(file_path)
    frames = []

    while True:
        ret, frame = video.read()
        if not ret:
            break
        frames.append(frame)

    video.release()
    return frames       