"""
module_base.py

Defines the abstract base classes (ABCs) that enforce the required structure
for all core modules within LiftOCR.

Each module in the OCR pipeline must inherit from its respective base class
and implement all required methods.

Location:
ocr/core/module_base.py
"""

from abc import ABC, abstractmethod


class BasePreprocessor(ABC):
    """Abstract base class for all preprocessors."""

    @abstractmethod
    def process(self, image):
        """Clean and prepare the input image.
        Args:
            image: Input image (usually a numpy array)
        Returns:
            Processed image (numpy array)
        """
        pass


class BaseSegmenter(ABC):
    """Abstract base class for all segmenters."""

    @abstractmethod
    def segment(self, image):
        """Split the image into lines, words, or characters.
        Args:
            image: Preprocessed image
        Returns:
            List of image segments (list of numpy arrays)
        """
        pass


class BaseRecognizer(ABC):
    """Abstract base class for all recognizers."""

    def __init__(self, config):
        self.config = config

    @abstractmethod
    def recognize(self, segments):
        pass



class BasePostprocessor(ABC):
    """Abstract base class for all postprocessors."""

    @abstractmethod
    def postprocess(self, text):
        """Clean and correct recognized text.
        Args:
            text: Raw recognized text
        Returns:
            Cleaned and corrected text
        """
        pass


class BaseOutput(ABC):
    """Abstract base class for all output modules."""

    @abstractmethod
    def save(self, text, output_path):
        """Save processed text to desired output format.
        Args:
            text: Final OCR output text
            output_path: File path to save output
        Returns:
            None
        """
        pass