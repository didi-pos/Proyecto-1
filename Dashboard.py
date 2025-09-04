import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Pepper Tech News", layout="wide")

# Título principal
st.markdown("<h1 style='text-align: center; color: white; background-color: #FFB703; padding: 15px; border-radius: 15px;'>🤖 Presentando Novedades Tecnológicas con Pepper</h1>", unsafe_allow_html=True)

st.write("")

# Layout principal con dos columnas
col1, col2 = st.columns([1, 2])

# ------------------- Columna Izquierda -------------------
with col1:
    st.image("https://i.imgur.com/tpepper.png", caption="Pepper Robot", use_column_width=True)

    st.markdown("<div style='text-align: center; margin-top: 15px;'>", unsafe_allow_html=True)
    if st.button("🎬 Iniciar Video"):
        st.video("https://www.youtube.com/watch?v=7LNLsQW1_9I")  # puedes cambiar el link
    st.markdown("</div>", unsafe_allow_html=True)

# ------------------- Columna Derecha -------------------
with col2:
    # Segmento 1
    with st.container():
        st.markdown("### 🔸 Novedad Tecnológica 1")
        st.info("Aquí puedes escribir una breve descripción de la novedad tecnológica 1.")

    st.write("")

    # Segmento 2
    with st.container():
        st.markdown("### 🔹 Novedad Tecnológica 2")
        st.success("Aquí puedes escribir una breve descripción de la novedad tecnológica 2.")

    st.write("")

    # Segmento 3
    with st.container():
        st.markdown("### 🟢 Novedad Tecnológica 3")
        st.warning("Aquí puedes escribir una breve descripción de la novedad tecnológica 3.")

# ------------------- Sección inferior -------------------
st.write("---")
col3, col4 = st.columns([2, 1])

with col3:
    st.markdown("💬 **¿Tienes dudas? Consulta con tu chatbot de confianza.**")
    pregunta = st.text_input("Escribe tu pregunta aquí:")
    if pregunta:
        st.success(f"Pepper dice: Estoy procesando tu duda sobre '{pregunta}'...")

with col4:
    st.image("https://i.imgur.com/6c9q6VN.png", caption="Asistente Virtual", use_column_width=True)
