"""
default.py

LiftOCR Default Segmenter Module

Purpose:
- Segment the preprocessed image into character regions
- Uses contour detection to find individual components

Location:
ocr/modules/segment/default.py
"""

import cv2
from ocr.core.module_base import BaseSegmenter


class DefaultSegmenter(BaseSegmenter):
    """Segment image using OpenCV contour detection."""

    def segment(self, image):
        print("[Segmenter] Running DefaultSegmenter")

        # Find contours of the thresholded image
        contours, _ = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        segments = []

        for contour in contours:
            x, y, w, h = cv2.boundingRect(contour)

            # Filter out tiny noise contours
            if w < 5 or h < 5:
                continue

            char_image = image[y:y+h, x:x+w]
            segments.append(char_image)

        print(f"[Segmenter] Found {len(segments)} segments")

        return segments
