import streamlit as st
import base64
from PIL import Image
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
background-image: url("https://www.raed.net/img?id=512139");
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

st.sidebar.markdown("إختبر نطقك للحروف")

import wave
import streamlit as st
import speech_recognition as sr
from audio_recorder_streamlit import audio_recorder
import pyaudio

arabic_letters = ['أ', 'ب', 'ت', 'ث', 'ج', 'ح', 'خ', 'د', 'ذ', 'ر', 'ز', 'س', 'ش', 'ص', 'ض', 'ط', 'ظ', 'ع', 'غ', 'ف', 'ق', 'ك', 'ل', 'م', 'ن', 'ه', 'و', 'ي']

def recognize_speech():
    recognizer = sr.Recognizer()

    # Get the number of available audio devices using pyaudio
    p = pyaudio.PyAudio()
    device_count = p.get_device_count()
   

    if device_count > 0:
        st.write("أحسنت إجابة صحيحة!", selected_letter)
        st.balloons()

        st.audio('/Users/renadamer/Downloads/stream/mainpage_app/إجابة صحيحة.mp3', format='audio/mp3')
        st.balloons()
        st.balloons()
        st.balloons()

        with sr.Microphone(device_index=0) as source:

            audio = recognizer.listen(source)

        try:
            
            audio_bytes = recognizer.recognize_google(audio, language="ar")
            st.write("الحرف المنطوق هو: ", audio_bytes)
            return audio_bytes
        except sr.UnknownValueError:
            return None
    else:
        st.write("إجابة خاطئة! الحرف الصحيح هو:", selected_letter)
        return None

st.title('إختبر نطقك ')

selected_letter = st.selectbox('اختر حرفًا', arabic_letters)

st.write("قم بتسجيل صوتك...")
audio_bytes = audio_recorder()
if audio_bytes:
    st.audio(audio_bytes, format="audio/wav")
    audio_bytes = recognize_speech()
    if audio_bytes:
        if audio_bytes == selected_letter:
            st.write("إجابة صحيحة!")
        else:
            st.write("إجابة خاطئة! الحرف الصحيح هو:", selected_letter)



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
        <a href="http://localhost:8501/page_5" class="custom-button">التالي</a>
        <a href=""http://localhost:8501/page_3" class="custom-button">السابق</a>
    </div>
    """
    , unsafe_allow_html=True
)




