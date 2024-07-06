import streamlit as st
from PIL import Image
import easyocr

# Function to extract text from image using easyocr
def extract_text_from_image(image):
    try:
        # Create easyocr Reader object
        reader = easyocr.Reader(['en'])
        # Convert image to numpy array and read text
        result = reader.readtext(image, detail=0)
        return result
    except Exception as e:
        return [str(e)]

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
