from ocr.core.module_base import BaseRecognizer


class ModelRecognizer(BaseRecognizer):
    """
    ML-Based Recognizer for LiftOCR

    Configuration YAML Example:

    recognizer: ocr.modules.recognize.model.ModelRecognizer
    recognizer_engine: easyocr
    """

    def __init__(self, config, engine="easyocr"):
        super().__init__(config)
        self.engine = engine

        # Initialize your ML OCR engine
        if self.engine == "easyocr":
            import easyocr
            self.reader = easyocr.Reader(["en"])

        elif self.engine == "tesseract":
            import pytesseract
            self.reader = pytesseract

        else:
            raise ValueError(f"Unknown OCR engine: {self.engine}")

    def recognize(self, segments):
        """
        Perform OCR on the provided segments (list of images).

        :param segments: List of images (numpy arrays)
        :return: Extracted text (string)
        """

        results = []

        for image in segments:
            if self.engine == "easyocr":
                text = self.reader.readtext(image, detail=0)
                results.append(" ".join(text))

            elif self.engine == "tesseract":
                import cv2
                gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                text = self.reader.image_to_string(gray)
                results.append(text.strip())

        return "\n".join(results)