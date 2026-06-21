# app/video/rebuild.py
import subprocess
from pathlib import Path

def concat_audios(audio_files, output_path):
    list_file = Path("audio_list.txt")
    with open(list_file, "w") as f:
        for af in audio_files:
            f.write(f"file '{af}'\n")

    cmd = [
        "ffmpeg", "-y",
        "-f", "concat", "-safe", "0",
        "-i", str(list_file),
        "-c", "copy",
        output_path
    ]
    subprocess.run(cmd, check=True)
    return output_path

def merge_video_audio(video_path, audio_path, output_path):
    cmd = [
        "ffmpeg", "-y",
        "-i", video_path,
        "-i", audio_path,
        "-c:v", "copy",
        "-c:a", "aac",
        "-shortest",
        output_path,
    ]
    subprocess.run(cmd, check=True)
    return output_path
