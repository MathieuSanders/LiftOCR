# LiftOCR

> *Recover the story. Lift the words.*

LiftOCR is a modular, open-source OCR framework designed for clean architecture, easy expansion, and flexible document OCR using machine learning (ML)-based recognition.

---

## Features

- Modular Python OCR pipeline
- ML-Based Recognizer using EasyOCR or Tesseract
- Abstract Base Classes (ABCs) enforce module structure
- Swappable components via YAML configuration
- Command-line interface with output folder override
- GPU acceleration supported with CUDA-backed PyTorch
- install_torch.py for smart PyTorch installation
- uninstall_torch.py for easy cleanup
- Clean software architecture & project management example

---

## Installation

Clone the repository:

```bash
git clone https://github.com/MathieuSanders/LiftOCR.git
cd LiftOCR
```

Install dependencies:

```bash
pip install -e .
```

Install the correct version of PyTorch based on your system:

```bash
python tools/install_torch.py
```

This script will:
- Detect your system's GPU (if any)
- Detect CUDA version
- Recommend the best PyTorch install option
- Handle CPU-only installs if no GPU is found

---

## Uninstall PyTorch (Optional)

To cleanly remove PyTorch, EasyOCR, and related packages:

```bash
python tools/uninstall_torch.py
```

This will:
- Uninstall torch, torchvision, torchaudio, easyocr, pytesseract
- Clear cached files from local storage
- Verify removal

---

## Usage

### Command-Line OCR Execution

Run LiftOCR from the command line:

```bash
python main.py --input path/to/image.jpg --output path/to/output_folder
```

Arguments:
- `--input` (required) = path to your input image
- `--output` (optional) = overrides output folder in config.yaml

Results will be saved as `.txt` file in the output folder.

---

## Configuration

Configuration file:

```
config/config.yaml
```

Control the pipeline flow:
- Preprocessor
- Segmenter
- Recognizer (ML-based)
- Postprocessor
- Output

Example:

```yaml
recognizer: ocr.modules.recognize.model.ModelRecognizer
recognizer_engine: easyocr   # or tesseract
output_path: output/
log_level: INFO
```

Ensure PyTorch is installed correctly for your chosen recognizer and engine.

---

## Documentation

Architecture decisions and design rationale:

```
docs/architecture.md
```

Project board and active development tracking:

📌 [LiftOCR Development Roadmap](https://github.com/MathieuSanders/LiftOCR/projects)

Wiki for guides, troubleshooting, and module reference:

📖 [LiftOCR Wiki](https://github.com/MathieuSanders/LiftOCR/wiki)

---

## License

MIT License

Copyright (c) 2025 Mathieu Sanders

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


