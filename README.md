# AI Tutorial Video Generator

## Overview

An AI-powered system that transforms raw screen recordings into structured, narrated tutorial videos automatically.

The application combines Computer Vision, OCR, Large Language Models, Text-to-Speech, and video processing technologies to detect user actions, extract on-screen information, generate tutorial instructions, and produce complete educational videos.

## Features

* Screen recording analysis
* UI action detection
* OCR text extraction using Tesseract
* Automated step generation using LLMs
* AI-generated voice narration
* Video reconstruction with FFmpeg
* FastAPI backend
* Interactive web interface

## Technologies Used

* Python
* FastAPI
* OpenCV
* Tesseract OCR
* FFmpeg
* OpenAI API
* ElevenLabs
* HTML/CSS
* Uvicorn

## Project Structure

```text
app/
├── analysis/
├── audio/
├── llm/
├── video/
├── main.py

static/
screenshots/
README.md
requirements.txt
```

## Workflow

1. Upload screen recording
2. Extract video frames
3. Detect UI interactions
4. Extract text using OCR
5. Generate tutorial steps using LLMs
6. Create AI voice narration
7. Rebuild video with narration
8. Export final tutorial video

## Skills Demonstrated

* Computer Vision
* OCR Processing
* Video Processing
* FastAPI Development
* AI Workflow Automation
* Prompt Engineering
* Backend Development
* API Integration
* System Design

## Business Applications

* Software Training Platforms
* Employee Onboarding
* Educational Content Creation
* SaaS Product Documentation
* Automated Tutorial Generation

## Author

Deborah Nehema
AI Engineer | Machine Learning Engineer | Python Developer
