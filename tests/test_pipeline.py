"""
test_pipeline.py

Integration Test for LiftOCR Pipeline

Purpose:
- Load a test image
- Run full OCR pipeline
- Validate non-empty output

Location:
tests/test_pipeline.py
"""

import os
import cv2
import yaml
import importlib


def load_class(import_path):
    module_name, class_name = import_path.rsplit(".", 1)
    module = importlib.import_module(module_name)
    return getattr(module, class_name)


def load_config():
    with open("config/config.yaml", 'r') as f:
        return yaml.safe_load(f)


def test_pipeline():
    """Run pipeline and check output is non-empty."""

    # Load sample image (provide your own test image path)
    test_image_path = "data/test_image.jpg"
    assert os.path.exists(test_image_path), f"Test image not found: {test_image_path}"

    config = load_config()

    preprocessor = load_class(config["preprocessor"])()
    segmenter = load_class(config["segmenter"])()
    recognizer = load_class(config["recognizer"])()
    postprocessor = load_class(config["postprocessor"])()

    image = cv2.imread(test_image_path)
    processed = preprocessor.process(image)
    segments = segmenter.segment(processed)
    raw_text = recognizer.recognize(segments)
    clean_text = postprocessor.postprocess(raw_text)

    assert isinstance(clean_text, str), "Output text is not a string"
    assert len(clean_text.strip()) > 0, "Output text is empty"

    print("[Test] Pipeline test passed.")