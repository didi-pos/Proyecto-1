import streamlit as st
import requests
from gtts import gTTS
import os

# Chatbot

API_KEY = os.getenv("DEEPSEEK_API_KEY")
API_URL = "https://api.deepseek.com/v1/chat/completions"

def enviar_mensaje(mensaje, modelo="deepseek-chat"):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
    }
    data = {
        "model": modelo,
        "messages": [
            {"role": "system", "content": "Eres un genio para la electrónica y para sistemas/software, enfocado en sistemas digitales con una actitud bastante inteligente y clara con lo que explica."}, 
            {"role": "user", "content": mensaje},
        ],
    }
    response = requests.post(API_URL, headers=headers, json=data)
    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        return f"Error: {response.text}"

def generar_audio(texto, filename="respuesta.mp3"):
    tts = gTTS(text=texto, lang="es")
    tts.save(filename)
    return filename

# Dashboard

st.set_page_config(page_title="Pepper Tech News", layout="wide")

st.markdown("<h1 style='text-align: center; color: white; background: linear-gradient(75deg, #2DB1C4, #0242A3); padding: 15px; border-radius: 15px;'>El reportero o reportera PEPPER</h1>", unsafe_allow_html=True)
st.write("")
col1, col2 = st.columns([1, 2])

# Primera Parte

with col1:
    st.markdown("<div style='text-align: center; margin-top: 15px;'>", unsafe_allow_html=True)
    if st.button("🎬 Iniciar Video"):
        st.video("https://www.youtube.com/watch?v=7LNLsQW1_9I")
    st.markdown("</div>", unsafe_allow_html=True)

# Segunda Parte

with col2:
    with st.container():
        st.markdown("### 🔴 Criptografía homomórfica práctica y su impacto en los sistemas digitales")
        st.info("Aquí puedes escribir una breve descripción de la novedad tecnológica 1.")
    st.write("")
    with st.container():
        st.markdown("### 🔵 DNA data storage y su impacto en los sistemas digitales")
        st.success("Aquí puedes escribir una breve descripción de la novedad tecnológica 2.")
    st.write("")
    with st.container():
        st.markdown("### 🟢 Interfaces hápticas de ultrasonido")
        st.warning("Aquí puedes escribir una breve descripción de la novedad tecnológica 3.")

# Tercera Parte

st.write("---")
st.markdown("## 💬 ¿Tienes dudas? Consulta con tu chatbot de confianza 🤖")

entrada = st.chat_input("Que dudas tienes sobre lo dicho por Pepper")

if st.button("Enviar") and entrada:
    respuesta = enviar_mensaje(entrada)
    st.markdown(f"**🤖 Chatbot:** {respuesta}")
    audio_file = generar_audio(respuesta)
    st.audio(audio_file, format="audio/mp3")
