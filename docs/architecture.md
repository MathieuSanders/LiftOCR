# LiftOCR Architecture & Design Decisions

*Document Owner: Mathieu Sanders*  
*Last Updated: 2025-04-15*

---

## Purpose of this Document
This document captures the architectural design decisions made during the development of LiftOCR. It provides historical context for technical choices, documents pivots in strategy, and ensures future contributors understand the rationale behind key components.

LiftOCR was intentionally built as a modular, extensible OCR framework — not just as a tool, but as a demonstration of clean software engineering and adaptability.

---

## Initial Architecture (v0.1 - v0.2 Pre-Pivot)

### Recognizer Design
- LiftOCR began with a `TemplateRecognizer` engine using:
  - OpenCV for image processing.
  - Contour detection for template matching.
  - Static expectations for layout positioning.

### Rationale
- Template-based recognition is simple to implement for highly structured documents.
- Fast, lightweight.
- Excellent for repeatable forms or known layouts.

---

## Pivot Decision: Move to ML-Based Recognizer

### Date of Decision
April 15, 2025 (During v0.2 Development)

### Why We Pivoted
| Problem | Impact |
|---------|--------|
| Template methods lack flexibility | Real-world documents vary too much |
| Hard-coded templates don't scale | Every new document type required manual effort |
| OCR industry standards use ML | Expected from modern OCR solutions |
| Maintainability concerns | Future contributors would struggle without extensive template documentation |

---

## New Recognizer Design (v0.2+)

- Introduction of `ModelRecognizer` module
- Abstract Base Class pattern remains intact
- Recognizer choice is YAML-driven
- ML Engine agnostic → EasyOCR or Tesseract initially
- Future-ready for custom-trained models

---

## Architectural Principles

| Principle | Implementation |
|-----------|----------------|
| Modularity | Recognizers are isolated in `ocr/modules/recognize/` |
| Configurability | YAML config controls component selection |
| Extensibility | Easy to add new Recognizers without breaking old code |
| Transparency | All design changes logged here |

---

## Directory Layout (As of 2025-04-14)

```
LiftOCR/
├── .git/
├── .pytest_cache/
├── config/
│   └─ config.yaml
├── data/
│   └─ test_image.jpg
├── docs/
│   └─ architecture.md
├── gui/
│   └─ app.py
├── LiftOCR.egg-info/
├── ocr/
│   


# END OF DOCUMENT
