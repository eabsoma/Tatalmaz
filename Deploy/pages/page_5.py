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
background-image: url("https://www.raed.net/img?id=513568");
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


import streamlit as st



st.sidebar.markdown("أهلاً بك في مساعدك التعليمي ")

from openai import OpenAI


st.title("مساعدي التعليمي ")

client = OpenAI(api_key=st.secrets["openai_api_key"])

if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("أهلا بك في مساعدك التعليمي تفضل بكتابة سؤالك "):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        for response in client.chat.completions.create(
            model=st.session_state["openai_model"],
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            stream=True,
        ):
            full_response += (response.choices[0].delta.content or "")
            message_placeholder.markdown(full_response + "▌")
        message_placeholder.markdown(full_response)
    st.session_state.messages.append({"role": "assistant", "content": full_response})
  

st.markdown(
    """
    <style>
    .button-container {
        display: flex;
        margin-top: 120px;
    }
    .custom-button {
        padding: 10px 20px;
        background-color: #EBA1A6;
        color: white; 
        border-radius: 20px;
        border: none;
        text-decoration: none;
        text-align: right; /* هنا تغيير موضع النص إلى اليمين */
    }
    </style>
    """
    , unsafe_allow_html=True
)

st.markdown(
    """
    <div class="button-container">
        <a href="http://localhost:8501/page_4" class="custom-button">السابق</a>
    </div>
    """
    , unsafe_allow_html=True
)





