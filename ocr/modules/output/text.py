"""
text.py

LiftOCR Text Output Module

Purpose:
- Save OCR result text to a .txt file

Location:
ocr/modules/output/text.py
"""

import os
from ocr.core.module_base import BaseOutput


class TextOutput(BaseOutput):
    """Saves OCR output text to a .txt file."""

    def save(self, text, output_path):
        print(f"[Output] Saving output to {output_path}")

        os.makedirs(os.path.dirname(output_path), exist_ok=True)

        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(text)

        print("[Output] Save complete.")