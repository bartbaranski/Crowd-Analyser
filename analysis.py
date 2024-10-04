from yolo_detection import detect_people

def analyze_video_frames(frames, update_gui_callback, skip_frames=2):
    total_people_count = 0
    frame_count = 0

    for i, frame in enumerate(frames):
        if i % skip_frames == 0:  # Przetwarzaj co trzecią klatkę
            people_count, processed_frame = detect_people(frame)
            total_people_count += people_count
            frame_count += 1

            # Wywołanie funkcji aktualizującej GUI z przetworzoną klatką
            update_gui_callback(processed_frame)

    return total_people_count, frame_count

