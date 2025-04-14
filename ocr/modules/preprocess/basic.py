"""
basic.py

LiftOCR Basic Preprocessor Module

Purpose:
- Clean and prepare the input image for OCR
- Applies grayscale conversion
- Thresholding for binarization
- Resizing for standardization

Location:
ocr/modules/preprocess/basic.py
"""

import cv2
from ocr.core.module_base import BasePreprocessor


class BasicPreprocessor(BasePreprocessor):
    """Basic image cleaning using OpenCV."""

    def process(self, image):
        print("[Preprocessor] Running BasicPreprocessor")

        # Convert to grayscale
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Apply thresholding to binarize the image
        _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)

        # Resize to a standard height (optional, good for OCR consistency)
        target_height = 800
        scale = target_height / thresh.shape[0]
        resized = cv2.resize(thresh, (int(thresh.shape[1] * scale), target_height))

        return resized