import pytesseract
import cv2
import streamlit as st
from PIL import Image
import numpy as np

def extract_text_from_image(image):
    # Convert the image to a NumPy array
    image = np.array(image)

    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Use Tesseract to extract text
    extracted_text = pytesseract.image_to_string(gray_image)

    return extracted_text

def main():
    st.title("Form Information Display")

    # Upload image
    uploaded_file = st.file_uploader("Choose an image file", type=["png", "jpg", "jpeg"])
    
    if uploaded_file is not None:
        # Read the image file
        image = Image.open(uploaded_file)

        # Extract text from the uploaded image
        form_text = extract_text_from_image(image)
        
        st.header("Extracted Information")
        st.text(form_text)

if __name__ == "__main__":
    main()
