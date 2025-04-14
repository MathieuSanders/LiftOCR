"""
template.py

LiftOCR Template Recognizer Module

Purpose:
- Recognize characters by template matching
- Requires a folder of pre-labeled character templates

Location:
ocr/modules/recognize/template.py
"""

import cv2
import os
from ocr.core.module_base import BaseRecognizer


class TemplateRecognizer(BaseRecognizer):
    """Recognizes characters by comparing them to template images."""

    def __init__(self, templates_path="templates"):
        print("[Recognizer] Initializing TemplateRecognizer")
        self.templates = self.load_templates(templates_path)

    def load_templates(self, templates_path):
        templates = {}
        if not os.path.exists(templates_path):
            print(f"[Recognizer] WARNING: No templates found at {templates_path}")
            return templates

        for filename in os.listdir(templates_path):
            if filename.endswith(".png") or filename.endswith(".jpg"):
                label = os.path.splitext(filename)[0]
                path = os.path.join(templates_path, filename)
                image = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
                templates[label] = image

        print(f"[Recognizer] Loaded {len(templates)} templates")
        return templates

    def recognize(self, segments):
        print("[Recognizer] Running TemplateRecognizer")

        recognized_text = ""

        for seg in segments:
            best_match = "?"
            best_score = 0

            for label, template in self.templates.items():
                resized = cv2.resize(seg, (template.shape[1], template.shape[0]))
                result = cv2.matchTemplate(resized, template, cv2.TM_CCOEFF_NORMED)
                _, score, _, _ = cv2.minMaxLoc(result)

                if score > best_score:
                    best_score = score
                    best_match = label

            recognized_text += best_match

        return recognized_text