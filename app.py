import streamlit as st
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Codigo CSS para mejorar los margenes de la pagina
st.markdown(
    """
    <style>
        .main .block-container {
            padding-left: 0px !important;
            padding-right: 0px !important;
            max-width: 100vw !important;
        }
        
        div[data-testid="column"] {
            flex-grow: 1 !important;
            flex-basis: 0 !important;
        }
    </style>
    """,
    unsafe_allow_html=True
)

analyzer = SentimentIntensityAnalyzer()

# Crear columnas de tamaño igual
col1, col2 = st.columns(2, gap="large")

with col1: #Columna para el chat IA de apoyo emocional
    st.title("Emotional Suport Chatot")

    if "respuestas" not in st.session_state:
        st.session_state.respuestas = []

    if "x" not in st.session_state:
        st.session_state.x = 0

    entrada = st.text_input("Tell me how you feel and I'll give you a personalized personality goal.")

    if entrada:
        resultado = analyzer.polarity_scores(entrada)
        respuesta = ""

        if resultado["neg"] > 0.5:
            respuesta = "I'm so sorry, it sounds like you're going through a tough time."
            objetivo = "Try to discover new hobbies that you like and that motivate you to learn and try to socialize more."
        elif resultado["neu"] > 0.5:
            respuesta = "Well, it could be worse. I hope things improve."
            objetivo = "You can try meeting new people and give yourself a change of scenery."
        elif resultado["pos"] > 0.5:
            respuesta = "I'm so glad you're feeling well."
            objetivo = "Take advantage of your time, study, read, and live your leisure time."
        else:
            respuesta = "Error in sentiment analysis."
            objetivo = "Try to express your thoughts more often. Talking about your emotions can help you manage them better."

        st.session_state.respuestas.insert(0, respuesta)
        st.session_state.x += 1

        st.write(respuesta)
        st.write(objetivo)
        st.write(f"Number of interactions: {st.session_state.x}")

        st.write("Previous answers:")
        for i, resp in enumerate(st.session_state.respuestas, 1):
            st.write(f"{i}. {resp}")
    else:
        st.write("Por favor, ingresa algo para que te pueda ayudar.")

with col2:
    st.title("emotions diary")
    entrada_2 = st.text_input("Tell me how you feel today")

    if "entradas_diario" not in st.session_state:
        st.session_state.entradas_diario = []

    if entrada_2:
        st.session_state.entradas_diario.append(entrada_2)

    if st.session_state.entradas_diario:
        for i, entr in enumerate(reversed(st.session_state.entradas_diario), start=1):
            st.write(f"Day {len(st.session_state.entradas_diario) - i + 1}: {entr}")

    else:
        st.write("There is no diary entries yet.")
