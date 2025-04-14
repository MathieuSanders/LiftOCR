"""
basic.py

LiftOCR Basic Postprocessor Module

Purpose:
- Clean up recognized text output
- Remove extra whitespace
- Normalize line breaks

Location:
ocr/modules/postprocess/basic.py
"""

from ocr.core.module_base import BasePostprocessor


class BasicPostprocessor(BasePostprocessor):
    """Simple post-processing of recognized text."""

    def postprocess(self, text):
        print("[Postprocessor] Running BasicPostprocessor")

        # Remove multiple spaces
        text = ' '.join(text.split())

        # Normalize line breaks (if needed in future)
        text = text.replace(" \n ", "\n")

        return text