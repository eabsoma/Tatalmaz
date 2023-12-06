import streamlit as st
import cv2
import pytesseract
from PIL import Image
import numpy as np
import base64
import plotly.express as px
import cv2

st.set_page_config(
    page_icon='/Users/renadamer/Downloads/stream/mainpage_app/logo1.png',
)

df = px.data.iris()

@st.cache_data
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()


img = get_img_as_base64("/Users/renadamer/Downloads/stream/logos.png")

page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("https://www.raed.net/img?id=504778");
background-size:100% 100%;
background-position: top left;
background-repeat: no-repeat;
background-attachment: local;
}}

[data-testid="stSidebar"] > div:first-child {{
#background-image: url("data:/Users/renadamer/Downloads/stream/logos.png;base64,{img}");
background-position: center; 
background-repeat: no-repeat;
background-attachment: fixed;
}}

[data-testid="stHeader"] {{
background: rgba(0,0,0,0);
}}

[data-testid="stToolbar"] {{
right: 2rem;
}}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)
st.sidebar.markdown(" إستخراج النصوص من الصور ")

pytesseract.pytesseract.tesseract_cmd = '/Users/renadamer/anaconda3/lib/python3.11/site-packages/pytesseract/pytesseract.py'



def perform_ocr(image):
    # Open the image using OpenCV
    img = cv2.imdecode(np.frombuffer(image.read(), np.uint8), -1)

    # Convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)



    # Use pytesseract to do OCR on the image
    extracted_text = pytesseract.image_to_string(gray, lang='ara')

    return extracted_text

def main():
    st.title('  : إستخراج النصوص من الصور ')


    # Upload image through Streamlit
    image = st.file_uploader("Upload Image", type=["jpg", "jpeg", "png"])

    if image is not None:
        # Display the uploaded image
        st.image(image, caption="Uploaded Image", use_column_width=True)

        # Perform OCR on the image
        extracted_text = perform_ocr(image)

        # Display the extracted text
        st.subheader("Extracted Text:")
        st.write(extracted_text)


if __name__ == "__main__":
    main()


st.markdown(
    """
    <style>
    .button-container {
        display: flex;
        justify-content: space-between;
        margin-top: 120px;
    }
    .custom-button {
        padding: 10px 20px;
        background-color: #EBA1A6;
        color: white; 
        border-radius: 20px;
        border: none;
        text-decoration: none;
    }
    </style>
    """
    , unsafe_allow_html=True
)

st.markdown(
    """
    <div class="button-container">
        <a href="http://localhost:8501/page_4" class="custom-button">التالي</a>
        <a href="http://localhost:8501/page_2" class="custom-button">السابق</a>
    </div>
    """
    , unsafe_allow_html=True
)

