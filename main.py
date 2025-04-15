"""
main.py

LiftOCR CLI Entry Point

- Loads config.yaml
- Dynamically imports pipeline modules
- Executes the OCR pipeline:
  preprocess -> segment -> recognize -> postprocess -> output

Usage:
python main.py --input path/to/image.jpg
"""

import argparse
import importlib
import yaml
import os


def load_class(import_path):
    """Dynamically load a class from a string import path."""
    module_name, class_name = import_path.rsplit(".", 1)
    module = importlib.import_module(module_name)
    return getattr(module, class_name)


def load_config():
    with open("config/config.yaml", 'r') as f:
        return yaml.safe_load(f)


def main():
    parser = argparse.ArgumentParser(description="LiftOCR - Modular OCR Pipeline")
    parser.add_argument("--input", required=True, help="Path to input image")
    args = parser.parse_args()

    config = load_config()

    preprocessor = load_class(config["preprocessor"])()
    segmenter = load_class(config["segmenter"])()

    # Recognizer supports engine configuration (for ML-based recognizers)
    recognizer_class = load_class(config["recognizer"])
    recognizer_kwargs = {}
    if recognizer_class.__name__ == "ModelRecognizer":
        recognizer_kwargs["engine"] = config.get("recognizer_engine", "easyocr")
    recognizer = recognizer_class(config, **recognizer_kwargs)

    postprocessor = load_class(config["postprocessor"])()
    output_module = load_class(config["output"])()

    image_path = args.input
    print("[LiftOCR] Loading image:", image_path)

    import cv2
    image = cv2.imread(image_path)

    processed = preprocessor.process(image)
    segments = segmenter.segment(processed)
    raw_text = recognizer.recognize(segments)
    clean_text = postprocessor.postprocess(raw_text)

    output_dir = config.get("output_path", "output")
    os.makedirs(output_dir, exist_ok=True)

    filename = os.path.splitext(os.path.basename(image_path))[0] + ".txt"
    output_path = os.path.join(output_dir, filename)

    output_module.save(clean_text, output_path)

    print(f"[LiftOCR] OCR complete. Output saved to: {output_path}")


if __name__ == "__main__":
    main()
