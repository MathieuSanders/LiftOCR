# LiftOCR Project Roadmap

This roadmap outlines the development milestones and current progress for LiftOCR.
Each milestone builds on the previous one to deliver a fully modular, extensible, and professional-grade OCR system.

---

## ✅ v0.1 — Architecture Established
- [x] Repository created and structured
- [x] Abstract Base Classes (ABCs) implemented
- [x] Config loader with YAML support
- [x] CLI pipeline runner (`main.py`) built
- [x] Editable install enabled via `setup.py`
- [x] Testing framework set up (`pytest`, `test_pipeline.py`)
- [x] Project board and milestone tracking configured

---

## 🚧 v0.2 — Minimal Working Pipeline (In Progress)
- [x] Implement `BasicPreprocessor`
- [x] Implement `DefaultSegmenter`
- [x] Implement `TemplateRecognizer`
- [x] Implement `BasicPostprocessor`
- [x] Implement `TextOutput`
- [x] Build `config.yaml` to control pipeline
- [x] Pass integration test with real image
- [ ] Add sample templates for recognizer
- [ ] Add example output to `/output/`

---

## 🔜 v0.3 — Functional Core Modules
- [ ] Improve accuracy of each module
- [ ] Tune parameters in `basic.py` for better OCR
- [ ] Add simple logging
- [ ] Allow command-line overrides of config

---

## 🔜 v0.4 — GUI Integration
- [x] Build Tkinter-based GUI (`gui/app.py`)
- [ ] GUI output display area
- [ ] Add progress bar / spinner
- [ ] File drop support (optional)

---

## 🔜 v0.5 — Robust Testing & Docs
- [ ] Add unit tests for each module
- [ ] Add coverage reports
- [ ] Finalize README.md
- [ ] Populate Wiki fully
- [ ] Add API Reference to Wiki

---

## 🧩 v1.1 — Plugin System for User Modules
- [ ] Design plugin loader interface
- [ ] Document how to write a custom module
- [ ] Add plugin examples to `ocr/plugins`

---

## 📦 v2.0 — Model-Based Recognizer
- [ ] Replace TemplateRecognizer with ML/AI model
- [ ] Add training + inference pipeline 
- [ ] Add pre-trained weights loader

---

## 🌐 v2.1 — Multi-Language Support 
- [ ] Add support for multiple alphabets
- [ ] Add language-specific configs

---

## ✍ v2.2 — Handwriting Recognition 
- [ ] Add optional handwriting recognizer module
- [ ] Tune segmenter for cursive characters

---

_This file is maintained as part of LiftOCR’s public-facing GitHub repository and Wiki._