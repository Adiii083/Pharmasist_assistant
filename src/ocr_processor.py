import cv2
import pytesseract

class PrescriptionOCR:
    def preprocess_image(self, image_path):
        img = cv2.imread(image_path)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        processed = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
        return processed

    def extract_text(self, image_path):
        processed_img = self.preprocess_image(image_path)
        text = pytesseract.image_to_string(processed_img)
        return text
