import cv2
from yolo_detection import detect_people

def analyze_video_frames(frames):
    total_people_count = 0
    frame_count = 0

    for frame in frames:
        people_count, processed_frame = detect_people(frame)
        total_people_count += people_count
        frame_count += 1

        # Wyświetlanie analizowanej klatki (opcjonalne)
        cv2.imshow('Processed Frame', processed_frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):  # Naciśnij 'q', aby przerwać wyświetlanie
            break

    cv2.destroyAllWindows()

    return total_people_count, frame_count
