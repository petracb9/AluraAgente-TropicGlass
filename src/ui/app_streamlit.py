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

if "pregunta" not in st.session_state:
    st.session_state.pregunta = ""

if "respuesta" not in st.session_state:
    st.session_state.respuesta = ""

if "salir" not in st.session_state:
    st.session_state.salir = False

st.title("🤖 Alura Agente")
st.subheader("Asistente Inteligente - TropicGlass")

st.write(
    "Realiza una consulta sobre políticas, compras, envíos, pagos o devoluciones."
)

pregunta = st.text_input(
    "Escribe tu pregunta:",
    key="pregunta"
)


col1, col2, col3 = st.columns(3)

with col1:
    consultar = st.button("Consultar")

with col2:
    nueva = st.button("Nueva consulta")

with col3:
    salir = st.button("Salir")


if consultar:

    if pregunta.strip():

        with st.spinner("Buscando respuesta..."):
            st.session_state.respuesta = responder(pregunta)

if nueva:

    st.session_state.clear()
    st.rerun()


if salir:

    st.session_state.respuesta = ""
    st.session_state.salir = True

      
if st.session_state.respuesta:

        st.success("Respuesta")      
        st.write(st.session_state.respuesta)

if st.session_state.salir:

        st.info(
            "Gracias por utilizar Alura Agente.\n\n"
            "Puede cerrar esta pestaña cuando lo desee."
        )