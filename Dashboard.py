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
            {"role": "system", "content": "Eres un genio para la electrónica y para sistemas/software, enfocado en sistemas digitales, sobre todo en los temas: Criptografía homomórfica práctica y su impacto en los sistemas digitales, DNA data storage y su impacto en los sistemas digitales eInterfaces hápticas de ultrasonido. Con una actitud bastante inteligente y clara con lo que explica."}, 
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

st.markdown("<h1 style='text-align: center; color: white; background: linear-gradient(75deg, #0242A3, #2DB1C4); padding: 15px; border-radius: 15px;'>El reportero o reportera PEPPER</h1>", unsafe_allow_html=True)
st.write("")
col1, col2 = st.columns([1, 2])

# Primera Parte

with col1:
    st.markdown("<div style='text-align: center; margin-top: 15px;'>", unsafe_allow_html=True)
    video_placeholder = st.empty()
    if st.button("🎬 Iniciar Video", use_container_width=True):
        video_placeholder.video("https://www.youtube.com/watch?v=7LNLsQW1_9I")
    st.markdown("</div>", unsafe_allow_html=True)

# Segunda Parte

with col2:
    with st.container():
        st.markdown("### 🔴 Criptografía homomórfica práctica y su impacto en los sistemas digitales")
        st.info("Permite realizar operaciones sobre datos cifrados sin necesidad de descifrarlos. Esto mejora la seguridad y privacidad en sistemas digitales, especialmente en la nube y servicios donde se manejan datos sensibles.")
    st.write("")
    with st.container():
        st.markdown("### 🔵 DNA data storage y su impacto en los sistemas digitales")
        st.success("Consiste en almacenar información digital dentro de moléculas de ADN. Ofrece una capacidad enorme y duradera de almacenamiento en comparación con los métodos tradicionales, lo que puede revolucionar cómo guardamos grandes volúmenes de datos en el futuro.")
    st.write("")
    with st.container():
        st.markdown("### 🟢 Interfaces hápticas de ultrasonido")
        st.warning("Usan ondas ultrasónicas para generar sensaciones táctiles en el aire, sin necesidad de contacto físico. Esto permite nuevas formas de interacción con dispositivos digitales, con aplicaciones en realidad virtual, medicina y accesibilidad.")

# Tercera Parte

st.write("---")
st.markdown("## 💬 ¿Tienes dudas? Consulta con tu chatbot de confianza 🤖")

entrada = st.chat_input("¿Que dudas tienes sobre los temas relacionado?")

if entrada:
    st.markdown(f"**👤 Tú:** {entrada}")
    respuesta = enviar_mensaje(entrada)
    st.markdown(f"**🤖 Chatbot:** {respuesta}")
    audio_file = generar_audio(respuesta)
    st.audio(audio_file, format="audio/mp3")
