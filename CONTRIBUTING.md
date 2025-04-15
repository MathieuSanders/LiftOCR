# Contributing to LiftOCR

Thank you for your interest in contributing to LiftOCR!

This project is designed to be clean, modular, and educational — a showcase of real-world Python software architecture for OCR (Optical Character Recognition).

---

## How to Contribute

1. Fork the repository on GitHub.
2. Create a new branch based on `main`:

```bash
git checkout -b feature/your-feature-name
```

3. Make your changes following the project structure.
4. Add or update tests if needed.
5. Run tests locally:

```bash
pytest tests/
```

6. Commit and push your changes:

```bash
git add .
git commit -m "Describe your change clearly"
git push origin feature/your-feature-name
```

7. Submit a Pull Request (PR) to the `main` branch.
8. Reference any related Issues in your PR description.

---

## Project Structure

| Folder | Purpose |
|--------|---------|
| `ocr/` | Core code modules |
| `config/` | YAML configuration files |
| `gui/` | GUI interface using Tkinter |
| `tests/` | Automated tests |
| `data/` | Test images or sample input |
| `output/` | OCR results |

---

## Coding Standards

- Follow PEP8 style guidelines.
- All modules must inherit from the appropriate Abstract Base Class (ABC).
- Add docstrings to all classes and functions.
- Keep code clean and simple.
- Avoid unnecessary complexity.

---

## Tests

All code must pass tests before being merged.

Test runner:
```bash
pytest
```

Integration Test:
```bash
pytest tests/test_pipeline.py
```

Add additional tests for new modules to `tests/`.

---

## Feature Ideas & Enhancements

Open an Issue to discuss:
- New ideas
- Bugs
- Architecture questions
- Improvements

---

## Licensing

By contributing, you agree that your contributions will be licensed under the MIT License.

---

Happy contributing!

- Mathieu Sanders
