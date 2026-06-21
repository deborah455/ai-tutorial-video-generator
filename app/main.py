from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pathlib import Path
import uuid
import shutil

from app.video.extract import extract_frames
from app.analysis.ui_detection import ocr_frame
from app.analysis.segmentation import simple_segment
from app.llm.steps import describe_steps
from app.audio.tts import generate_step_audios
from app.video.rebuild import concat_audios, merge_video_audio

app = FastAPI()


app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", include_in_schema=False)
async def root():
    return FileResponse("static/index.html")


@app.post("/process")
async def process_video(file: UploadFile = File(...)):
    # 1. Save uploaded video
    session_id = str(uuid.uuid4())
    work_dir = Path("sessions") / session_id
    work_dir.mkdir(parents=True, exist_ok=True)

    video_path = work_dir / file.filename
    with open(video_path, "wb") as f:
        shutil.copyfileobj(file.file, f)

    # 2. Extract frames
    frames = extract_frames(str(video_path), str(work_dir / "frames"))

    # 3. OCR + build frames_data
    frames_data = []
    for frame_path, timestamp in frames:
        text = ocr_frame(frame_path)
        frames_data.append({
            "frame_path": frame_path,
            "timestamp": timestamp,
            "text": text,
            "cursor": None,  # TODO: cursor detection
        })

    # 4. Segment into steps
    steps = simple_segment(frames_data)

    # 5. Describe steps (English for now)
    step_texts = describe_steps(steps, language="English")

    # 6. Generate TTS for each step
    audio_files = generate_step_audios(step_texts, base_dir=work_dir / "audio")

    # 7. Concatenate audio and merge with video
    all_audio = concat_audios(audio_files, str(work_dir / "all_steps.mp3"))
    output_video = work_dir / "tutorial_output.mp4"
    merge_video_audio(str(video_path), all_audio, str(output_video))

    return FileResponse(str(output_video), filename="tutorial_output.mp4")
