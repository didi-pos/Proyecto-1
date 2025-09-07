import streamlit as st
import requests
from gtts import gTTS
import os

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
            {"role": "system", "content": "Eres un genio para la electrónica y sistemas digitales."}, 
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

# -------- UI --------
st.markdown("## 💬 Chat con Pepper")

col1, col2 = st.columns([4,1])
with col1:
    user_input = st.text_input("Escribe tu pregunta:", key="input_text")

with col2:
    c1, c2 = st.columns(2)
    with c1:
        send_btn = st.button("📩 Enviar")
    with c2:
        mic_btn = st.button("🎤 Audio")

# -------- lógica --------
if send_btn and user_input:
    st.markdown(f"**👤 Tú:** {user_input}")
    respuesta = enviar_mensaje(user_input)
    st.markdown(f"**🤖 Pepper:** {respuesta}")
    audio_file = generar_audio(respuesta)
    st.audio(audio_file, format="audio/mp3")

if mic_btn:
    st.info("🎤 Aquí iría la lógica de reconocimiento de voz (se puede integrar con Web Speech API o librerías externas).")
