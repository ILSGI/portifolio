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
        "sql": "Structured query language (SQL) is the language used to manipulate, verify, and manage databases/relational databases. I use this language in the vast majority of my projects.",
        "ingles": "english",
        "espanhol": "Spanish"
    },
    "pt": {
        "titulo": "Competências",
        "python": "Como uma das linguagens que utilizo, o Python me auxilia muito em sua facilidade para automações e visualização por meio do Streamlit, como nesse portfólio. Também tenho conhecimento de diferentes bibliotecas como: NumPy, Pandas, Streamlit, etc.",
        "sql": "Structured query language (SQL) é a linguagem usada para manipular, verificar e gerenciar BDs/SGBDs. Utilizo essa linguagem na grande maioria dos meus projetos.",
        "ingles": "inglês",
        "espanhol": "espanhol"
    },
    "es": {
        "titulo": "Competencias",
        "python": "Como una de las lenguajes que utilizo, Python me ayuda mucho en su facilidad para automatizaciones y visualización a través de Streamlit, como en este portafolio. También tengo conocimiento de diferentes bibliotecas como: NumPy, Pandas, Streamlit, etc.",
        "sql": "El lenguaje de consulta estructurado (SQL) es el lenguaje utilizado para manipular, verificar y administrar bases de datos/sistemas de gestión de bases de datos relacionales. Utilizo este lenguaje en la gran mayoría de mis proyectos.",
        "ingles": "Inglés",
        "espanhol": "Español"
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
    sql = get_string(idioma, "sql")
    st.write(sql)
    
st.text("Inglés")
Inglés_df_data = [["total","B2"],["comprensión lectora","B2"],["comprensión auditiva","C1"],["expresión escrita","B1"],["expresión oral","B2"]]
def createDataframe(Inglés_df_data: [[int]]) -> pd.DataFrame:
    column_names = ['Inglés', 'nivel de idioma']
    sla = pd.DataFrame(Inglés_df_data, columns=column_names)
    return sla
df_es = createDataframe(Inglés_df_data)
st.table(df_es)

st.text("españhol")
espanhol_df_data = [["total","A2"],["comprensión lectora","B1"],["comprensión auditiva","B1"],["expresión escrita","A2"],["expresión oral","A2"]]
def createDataframe(espanhol_df_data: [[int]]) -> pd.DataFrame:
    column_names = ['españhol', 'nivel de idioma']
    sla = pd.DataFrame(espanhol_df_data, columns=column_names)
    return sla
df_es = createDataframe(espanhol_df_data)
st.table(df_es)
