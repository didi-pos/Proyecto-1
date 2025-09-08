import streamlit as st
import requests
from gtts import gTTS
from streamlit_mic_recorder import speech_to_text
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
            {"role": "system", "content": "Eres un genio para la electrónica y para sistemas/software, enfocado en sistemas digitales, sobre todo en los temas: Criptografía homomórfica práctica y su impacto en los sistemas digitales, DNA data storage y su impacto en los sistemas digitales e Interfaces hápticas de ultrasonido. Con una actitud bastante inteligente y clara con lo que explica."}, 
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
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    video_placeholder = st.empty()
    if st.button("🎬 Iniciar Video", use_container_width=True):
        video_placeholder.video(
            "https://youtu.be/WbXeMxcVCuY?si=o4GHMz8mb1nJjh8S", 
            format="video/mp4", 
            start_time=0
        )

# Segunda Parte
with col2:
    with st.container():
        st.markdown("### 🔴 Criptografía homomórfica práctica y su impacto en los sistemas digitales")
        st.info("La criptografía homomórfica permite **realizar operaciones matemáticas directamente sobre datos cifrados**, obteniendo un resultado que, al descifrarse, es el mismo que si se hubiera operado con los datos originales. Esto abre enormes posibilidades en seguridad y privacidad: hospitales, bancos y servicios en la nube pueden analizar información sensible sin nunca verla en claro. Así, protege datos personales y corporativos en un mundo cada vez más interconectado.")
    st.write("")
    with st.container():
        st.markdown("### 🔵 DNA data storage y su impacto en los sistemas digitales")
        st.success("El almacenamiento en ADN busca guardar información digital dentro de moléculas biológicas. Cada gramo de ADN puede almacenar hasta **215 millones de GB**, siendo una solución prácticamente ilimitada y estable durante miles de años. Frente a la creciente demanda de datos en la era digital, esta tecnología podría sustituir a los discos duros tradicionales, ofreciendo sostenibilidad, durabilidad y eficiencia energética.")
    st.write("")
    with st.container():
        st.markdown("### 🟢 Interfaces hápticas de ultrasonido")
        st.warning("Las interfaces hápticas de ultrasonido generan sensaciones táctiles en el aire mediante ondas ultrasónicas, **sin necesidad de contacto físico**. Esto permite que el usuario “sienta” botones o superficies virtuales flotando en el espacio. Sus aplicaciones incluyen realidad virtual inmersiva, control médico sin contacto (como en cirugías estériles) y sistemas accesibles para personas con discapacidad visual, abriendo un nuevo paradigma de interacción humano-computadora.")

# Tercera Parte
st.write("---")
st.markdown("## 💬 ¿Tienes dudas? Consulta con tu chatbot de confianza 🤖")
col1, col2 = st.columns([1, 5])

with col1:
    from streamlit_mic_recorder import speech_to_text
    voice_text = speech_to_text(
        language="es",
        just_once=True,
        use_container_width=True,
        key="voz",
    )
with col2:
    entrada = st.chat_input("Escribe aquí tu pregunta...")

if entrada or voice_text:
    texto_usuario = entrada if entrada else voice_text
    st.markdown(f"**👤 Tú:** {texto_usuario}")
    respuesta = enviar_mensaje(texto_usuario)
    st.markdown(f"**🤖 Chatbot:** {respuesta}")
    audio_file = generar_audio(respuesta)
    st.audio(audio_file, format="audio/mp3")
