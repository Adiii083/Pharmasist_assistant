import spacy
import re

class PrescriptionAnalyzer:
    def __init__(self):
        self.nlp = spacy.load("en_core_web_sm")

    def parse_prescription(self, text):
        doc = self.nlp(text)
        medications = []
        for ent in doc.ents:
            if ent.label_ == "CHEMICAL":
                med = {
                    "name": ent.text,
                    "dosage": self._extract_dosage(ent.sent.text),
                    "frequency": self._extract_frequency(ent.sent.text)
                }
                medications.append(med)
        return medications

    def _extract_dosage(self, text):
        match = re.search(r'\d+\s?(mg|g|ml)', text)
        return match.group(0) if match else "N/A"

    def _extract_frequency(self, text):
        match = re.search(r'\d+\s?(times daily|xdaily)', text)
        return match.group(0) if match else "N/A"
