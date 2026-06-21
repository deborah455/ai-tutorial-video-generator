# app/video/extract.py
import cv2
from pathlib import Path

def extract_frames(video_path: str, output_dir: str, frame_skip: int = 5):
    """
    Extract frames from a video every `frame_skip` frames.
    Returns list of (frame_path, timestamp_in_seconds).
    """
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        raise RuntimeError(f"Unable to open video: {video_path}")

    frame_idx = 0
    results = []

    fps = cap.get(cv2.CAP_PROP_FPS)
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        if frame_idx % frame_skip == 0:
            timestamp = frame_idx / fps
            frame_file = output_dir / f"frame_{frame_idx:06d}.png"
            cv2.imwrite(str(frame_file), frame)
            results.append((str(frame_file), timestamp))

        frame_idx += 1

    cap.release()
    return results
