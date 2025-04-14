# LiftOCR

> *Recover the story. Lift the words.*

LiftOCR is a modular, open-source OCR framework designed for clean architecture, easy expansion, and document OCR.

---

## Features

- Modular Python OCR pipeline
- Abstract Base Classes (ABCs) enforce module structure
- Swappable components via YAML configuration
- Command-line and GUI interfaces
- Real-world software architecture and project management example
- Designed to be extended with user-written modules

---

## Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/MathieuSanders/LiftOCR.git
cd LiftOCR
pip install -e .
```

Or use the requirements file:

```bash
pip install -r requirements.txt
```

---

## Usage

### Command-Line

Run LiftOCR from the command line:

```bash
python main.py --input path/to/image.jpg
```

- Replace `path/to/image.jpg` with your image file path.
- Output will be saved as a `.txt` file in the configured `output/` folder.

### GUI

Run LiftOCR using the GUI interface:

```bash
python gui/app.py
```

- A window will allow you to select your image file.
- OCR results will be displayed or saved automatically.

---

## Project Management

All planning and development activity is tracked in the GitHub Project board:

📌 [LiftOCR Development Roadmap](https://github.com/MathieuSanders/LiftOCR/projects)

This public project board tracks:

- Features
- Architecture decisions
- Active module development
- Testing and documentation goals

It reflects the same discipline used in professional software teams.

---

## Documentation

Comprehensive documentation is hosted in the GitHub Wiki:

📖 [LiftOCR Wiki](https://github.com/MathieuSanders/LiftOCR/wiki)

---

## License

MIT License

Copyright (c) 2024 Mathieu Sanders

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
