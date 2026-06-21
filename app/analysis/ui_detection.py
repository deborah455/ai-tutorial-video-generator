# app/analysis/ui_detection.py
import pytesseract
from PIL import Image
import cv2
import numpy as np

def ocr_frame(frame_path: str) -> str:
    """
    Return detected text from a frame image.
    """
    img = Image.open(frame_path)
    text = pytesseract.image_to_string(img)
    return text
def find_cursor(frame_path: str, cursor_template_path: str, threshold: float = 0.8):
    frame = cv2.imread(frame_path)
    template = cv2.imread(cursor_template_path)

    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

    res = cv2.matchTemplate(frame_gray, template_gray, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    if max_val >= threshold:
        h, w = template_gray.shape
        # top-left corner of cursor
        return (max_loc[0], max_loc[1], w, h, max_val)
    return None