from ocr.core.module_base import BaseModule

# Optional - Choose your engine
# import easyocr
# import pytesseract
# import cv2


class ModelRecognizer(BaseModule):
    """
    ML-Based Recognizer for LiftOCR

    Configuration YAML Example:

    recognize:
      type: model
      engine: easyocr
    """

    def __init__(self, config):
        super().__init__(config)
        self.engine = config.get("engine", "easyocr")

        # Initialize your ML OCR engine
        if self.engine == "easyocr":
            import easyocr
            self.reader = easyocr.Reader(["en"])
        elif self.engine == "tesseract":
            import pytesseract
            self.reader = pytesseract
        else:
            raise ValueError(f"Unknown OCR engine: {self.engine}")

    def execute(self, image):
        """
        Perform OCR on the provided image.

        :param image: Input image (numpy array or filepath)
        :return: Extracted text (string)
        """

        # EasyOCR example
        if self.engine == "easyocr":
            results = self.reader.readtext(image, detail=0)
            return " ".join(results)

        # Tesseract example
        elif self.engine == "tesseract":
            import cv2
            import pytesseract
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            text = pytesseract.image_to_string(gray)
            return text

        return ""
