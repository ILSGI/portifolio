import streamlit as st 


st.set_page_config(
    page_title="Lincoln - competencias",
    page_icon=""
)

idioma = st.sidebar.selectbox("escolha o idioma", ['pt', 'en', 'es'])

strings = {
    "en": {
        "titulo": "Competencies",
        "python": "As one of the languages I use, Python helps me a lot in its ease of automation and visualization through Streamlit, as in this portfolio. I also have knowledge of different libraries such as: NumPy, Pandas, Streamlit, etc.",
        "sql": "Structured query language (SQL) is the language used to manipulate, verify, and manage databases/relational databases. I use this language in the vast majority of my projects."
    },
    "pt": {
        "titulo": "Competências",
        "python": "Como uma das linguagens que utilizo, o Python me auxilia muito em sua facilidade para automações e visualização por meio do Streamlit, como nesse portfólio. Também tenho conhecimento de diferentes bibliotecas como: NumPy, Pandas, Streamlit, etc.",
        "sql": "Structured query language (SQL) é a linguagem usada para manipular, verificar e gerenciar BDs/SGBDs. Utilizo essa linguagem na grande maioria dos meus projetos."
    },
    "es": {
        "titulo": "Competencias",
        "python": "Como una de las lenguajes que utilizo, Python me ayuda mucho en su facilidad para automatizaciones y visualización a través de Streamlit, como en este portafolio. También tengo conocimiento de diferentes bibliotecas como: NumPy, Pandas, Streamlit, etc.",
        "sql": "El lenguaje de consulta estructurado (SQL) es el lenguaje utilizado para manipular, verificar y administrar bases de datos/sistemas de gestión de bases de datos relacionales. Utilizo este lenguaje en la gran mayoría de mis proyectos."
    }
}


def get_string(idioma, key):
    return strings[idioma][key]

titulo = get_string(idioma,"titulo")
st.title(titulo)

with st.expander("python"):
    python = get_string(idioma, "python")
    st.write(python)
    
with st.expander("sql"):
    "structured query lenguage é a linguagem usada para manipular, verificar e gerenciar BDs/SGBDs ultilizo essa linguagem na grande maioria dos meus projetos"
    
with st.expander("vou add mais"):
    "pedir ajuda a fernanda"
    
with st.expander("ingles"):
    "pedir ajuda a fernanda"
    
with st.expander("espanhol"):
    "pedir ajuda a luciana"
    
    