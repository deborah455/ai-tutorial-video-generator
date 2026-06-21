# app/analysis/segmentation.py
from typing import List, Dict, Any

def simple_segment(frames_data: List[Dict[str, Any]], text_change_threshold: int = 20):
    """
    frames_data: list of dicts like:
      {
        "frame_path": str,
        "timestamp": float,
        "text": str,
        "cursor": (x, y) or None
      }
    """
    steps = []
    if not frames_data:
        return steps

    current_step = {
        "start": frames_data[0]["timestamp"],
        "end": frames_data[0]["timestamp"],
        "frames": [frames_data[0]],
    }

    prev_text = frames_data[0]["text"]

    for fd in frames_data[1:]:
        cur_text = fd["text"] or ""
        # crude difference measure
        diff = abs(len(cur_text) - len(prev_text))

        if diff > text_change_threshold:
            # close current step
            current_step["end"] = fd["timestamp"]
            steps.append(current_step)

            # start new step
            current_step = {
                "start": fd["timestamp"],
                "end": fd["timestamp"],
                "frames": [fd],
            }
        else:
            current_step["end"] = fd["timestamp"]
            current_step["frames"].append(fd)

        prev_text = cur_text

    steps.append(current_step)
    return steps
