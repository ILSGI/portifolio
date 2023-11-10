import streamlit as st 


st.set_page_config(
    page_title="Lincoln - contato",
    page_icon="☭"
)

idioma = st.sidebar.selectbox("escolha o idioma", ['pt', 'en', 'es'])

strings = {
    "en": {
        "contato": "contact",
        "midias sociais": "social midia"
    },
    "pt": {
        "contato": "contato",
        "midias sociais": "midias sociais"
    },
    "es": {
        "contato": "Contacto",
        "midias sociais": "redes sociales"
    }
}

def get_string(idioma, key):
    return strings[idioma][key]

contato = get_string(idioma,"contato")
midias_sociais = get_string(idioma,"midias sociais")

st.title(contato)

st.subheader("📞: +55 (31) 99990-0807")
st.subheader("✉️: lincoln.sales.goncalves1@gmail.com")

st.title(midias_sociais)

st.subheader("github: https://github.com/ILSGI")
st.subheader("stackoverflow: https://stackoverflow.com/users/22666790/ilsgi")
st.link_button(DIO profille,"https://www.dio.me/users/lincoln_sales_goncalves1")
