import streamlit as st
from src.ocr_processor import PrescriptionOCR
from src.prescription_parser import PrescriptionAnalyzer
from src.order_manager import OrderManager
import sqlite3
import os

def main():
    st.title("Pharmacist's Assistant")
    uploaded_file = st.file_uploader("Upload Prescription", type=["jpg", "png"])
    if uploaded_file:
        with open("temp.jpg", "wb") as f:
            f.write(uploaded_file.getbuffer())
        st.image(uploaded_file, caption="Uploaded Prescription", use_column_width=True)
        try:
            ocr = PrescriptionOCR()
            text = ocr.extract_text("temp.jpg")
            st.subheader("Extracted Text")
            st.text(text)
            analyzer = PrescriptionAnalyzer()
            medications = analyzer.parse_prescription(text)
            st.subheader("Identified Medications")
            if medications:
                for med in medications:
                    st.write(f"**{med['name']}** - {med['dosage']} ({med['frequency']})")
            else:
                st.warning("No medications identified. Please try a clearer image if possible.")
            if st.button("Generate Order"):
                manager = OrderManager("data/medications.db")
                manager.create_order(medications)
                st.success("Order created successfully!")
        except Exception as e:
            st.error(f"An error occurred while processing the prescription: {str(e)}")
        finally:
            if os.path.exists("temp.jpg"):
                os.remove("temp.jpg")

if __name__ == "__main__":
    main()
