#streamlit
import streamlit as st

st.set_page_config(page_title="Formulario de Investigación", layout="centered")

st.title("Formulario Interactivo: Taller de Investigación I")

st.markdown("Responde las siguientes preguntas sobre metodología de investigación:")

with st.form("formulario_investigacion"):
    p1 = st.text_input("1. ¿Cuáles son las etapas del método científico?")

    p2 = st.radio(
        "2. Tipo de investigación que utiliza herramientas de análisis matemático y estadístico para describir, explicar y predecir fenómenos mediante datos numéricos",
        ["Investigación cualitativa", "Investigación exploratoria", "Investigación cuantitativa", "Investigación mixta"]
    )

    p3 = st.radio(
        "3. Tipo de investigación que se enfoca en mostrar las características de un fenómeno, grupo o situación, sin intentar explicar las causas o relaciones",
        ["Investigación experimental", "Investigación exploratoria", "Investigación descriptiva", "Investigación explicativa"]
    )

    p4 = st.radio(
        "4. Son cruciales para garantizar que los estudios se realicen de manera responsable y justa, respetando los derechos de los participantes y la integridad científica",
        ["Fundamentos científicos", "Principios éticos de la investigación", "Normas operativas", "Objetivos de estudio"]
    )

    p5 = st.radio(
        "5. Tipo de variables cuando se plantean hipótesis en la investigación",
        ["Variables controladas y no controladas", "Variables dependiente e independiente", "Variables internas", "Variables abstractas"]
    )

    p6 = st.text_input("6. ¿Cómo se llama al conjunto de pasos como identificar el problema, evaluar fuentes, crear hipótesis, recolectar y analizar datos, y redactar el informe?")

    submit = st.form_submit_button("Enviar respuestas")

    if submit:
        st.success("¡Respuestas enviadas con éxito!")
        st.markdown("### Tus respuestas:")
        st.write(f"1. {p1}")
        st.write(f"2. {p2}")
        st.write(f"3. {p3}")
        st.write(f"4. {p4}")
        st.write(f"5. {p5}")
        st.write(f"6. {p6}")
