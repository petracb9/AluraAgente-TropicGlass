import os
import sys

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

import streamlit as st

from agents.agente_rag import responder


st.set_page_config(
    page_title="Alura Agente - TropicGlass",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 Alura Agente")
st.subheader("Asistente Inteligente - TropicGlass")

st.write(
    "Realiza una consulta sobre políticas, compras, envíos, pagos o devoluciones."
)

pregunta = st.text_input(
    "Escribe tu pregunta:"
)

if st.button("Consultar"):

    if pregunta.strip():

        with st.spinner("Buscando respuesta..."):

            respuesta = responder(pregunta)

        st.success("Respuesta")

        st.write(respuesta)

    else:

        st.warning("Ingrese una pregunta.")