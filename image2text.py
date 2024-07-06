import streamlit as st
from PIL import Image
import easyocr
import numpy as np

@st.cache_resource
def load_easyocr_reader():
    return easyocr.Reader(['en'], verbose=False)

def extract_text_from_image(image):
    reader = load_easyocr_reader()
    image_np = np.array(image)
    result = reader.readtext(image_np, detail=0)
    return result

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
        st.text("\n".join(form_text))

if __name__ == "__main__":
    main()
