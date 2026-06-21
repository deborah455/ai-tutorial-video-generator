# app/audio/tts.py
import subprocess
from pathlib import Path
from typing import List

def text_to_speech(text: str, output_path: str) -> str:
    """
    Offline TTS using espeak to generate WAV, then convert to MP3 with ffmpeg.
    No API keys, no payment.
    """
    output_path = Path(output_path)
    tmp_wav = output_path.with_suffix(".wav")
    output_path.parent.mkdir(parents=True, exist_ok=True)

    # Generate WAV with espeak
    # -s = speed (150 is normal-ish), -v = voice (e.g. en for English)
    subprocess.run(
        ["espeak", "-s", "150", "-v", "en", text, "-w", str(tmp_wav)],
        check=True
    )

    # Convert WAV → MP3 using ffmpeg
    subprocess.run(
        ["ffmpeg", "-y", "-i", str(tmp_wav), str(output_path)],
        check=True
    )

    # Clean up temp wav
    tmp_wav.unlink(missing_ok=True)

    return str(output_path)


def generate_step_audios(step_texts: List[str], base_dir="outputs/audio") -> List[str]:
    """
    Create one audio file per step using the offline espeak TTS.
    """
    base = Path(base_dir)
    base.mkdir(parents=True, exist_ok=True)

    audio_files = []
    for i, text in enumerate(step_texts, start=1):
        audio_path = base / f"step_{i:03d}.mp3"
        text_to_speech(text, str(audio_path))
        audio_files.append(str(audio_path))

    return audio_files


if __name__ == "__main__":
    # quick test
    demo_dir = "outputs/test_audio"
    Path(demo_dir).mkdir(parents=True, exist_ok=True)
    print("Generating test audio...")
    generate_step_audios(["Hello, this is a test step."], base_dir=demo_dir)
    print(f"Check the folder: {demo_dir}")
