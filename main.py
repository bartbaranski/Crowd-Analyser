from db import add_video
from video_processing import process_video
from analysis import analyze_video_frames

def analyze_video(file_path):
    video_id = add_video(file_path, "mp4")
    frames = process_video(file_path)

    total_people, frame_count = analyze_video_frames(frames)
    
    fps = 30
    video_duration_minutes = len(frames) / (fps * 60)
    avg_people_per_minute = total_people / video_duration_minutes

    print(f"All Counted people: {total_people}")
    print(f"Avg Counted people per minute: {avg_people_per_minute:.2f}")

if __name__ == "__main__":
    analyze_video("data/sample_video.mp4")