"""
app.py

LiftOCR GUI Interface

Purpose:
- Allow users to select image file
- Run full OCR pipeline
- Display or save output

Location:
gui/app.py
"""

import tkinter as tk
from tkinter import filedialog, messagebox
import os
import yaml
import importlib
import cv2


def load_class(import_path):
    module_name, class_name = import_path.rsplit(".", 1)
    module = importlib.import_module(module_name)
    return getattr(module, class_name)


def load_config():
    with open("config/config.yaml", 'r') as f:
        return yaml.safe_load(f)


def run_pipeline(image_path):
    config = load_config()

    preprocessor = load_class(config["preprocessor"])()
    segmenter = load_class(config["segmenter"])()
    recognizer = load_class(config["recognizer"])()
    postprocessor = load_class(config["postprocessor"])()
    output_module = load_class(config["output"])()

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

    return output_path


def open_file():
    file_path = filedialog.askopenfilename(
        title="Select Image",
        filetypes=[("Image Files", "*.png *.jpg *.jpeg *.bmp")]
    )
    if file_path:
        try:
            output_path = run_pipeline(file_path)
            messagebox.showinfo("Success", f"OCR complete. Output saved to:\n{output_path}")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred:\n{e}")


def main():
    root = tk.Tk()
    root.title("LiftOCR")
    root.geometry("300x150")

    label = tk.Label(root, text="LiftOCR - Select an image file")
    label.pack(pady=10)

    btn = tk.Button(root, text="Browse...", command=open_file)
    btn.pack(pady=10)

    root.mainloop()


if __name__ == "__main__":
    main()