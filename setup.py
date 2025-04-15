from setuptools import setup, find_packages

setup(
    name="LiftOCR",
    version="0.2.0",
    author="Mathieu Sanders",
    description="A modular, open-source OCR framework for clean architecture and easy expansion using ML-based recognition.",
    packages=find_packages(exclude=["tests", "data"]),
    include_package_data=True,
    install_requires=[
        "opencv-python",
        "PyYAML",
        "easyocr",
        "pytesseract",
        "torch"
    ],
    python_requires='>=3.8',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)