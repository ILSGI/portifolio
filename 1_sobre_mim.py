import streamlit as st 

st.set_page_config(
    page_title="Lincoln - sobre mim",
    page_icon="☭"
)
 
idioma = st.sidebar.selectbox("escolha o idioma", ['pt', 'en', 'es'])


strings = {
    "en": {
        "titulo": "About me",
        "texto": "Hello, I'm Lincoln, a young man born in 2017. Every story has its first step, I want to start mine in data science. I have two passions in my life: sports and technology. Both of these passions have taught me many things: sports help me with teamwork, drive, discipline, and how to love and deal with challenges. On the technology side, I've learned to acquire information, deal with stress, and think logically. I believe that this portfolio is the first step towards a transformative future, uniting passion and career is the dream of many and I believe I can achieve it."
    },
    "pt": {
        "titulo": "Sobre mim",
        "texto": "Olá, sou o Lincoln, um jovem nascido em 2017. Toda história tem seu primeiro passo, desejo iniciar a minha na ciência de dados. Tenho duas paixões na minha vida: esportes e tecnologia. Ambas as histórias têm me ensinado diversas coisas: os esportes me ajudam com trabalho em equipe, disposição, disciplina e como amar e lidar com desafios. Por parte da tecnologia: aprendi a adquirir informação, lidar com estresse e a pensar de maneira lógica. Acredito que esse portfólio é o primeiro passo em direção a um futuro transformador, unir paixão e carreira é o sonho de muitos e acredito poder realizá-lo."
    },
    "es": {
        "titulo": "Sobre mí",
        "texto": "Hola, soy Lincoln, un joven nacido en 2017. Cada historia tiene su primer paso, deseo comenzar la mía en ciencia de datos. Tengo dos pasiones en mi vida: los deportes y la tecnología. Ambas pasiones me han enseñado muchas cosas: los deportes me ayudan con el trabajo en equipo, el impulso, la disciplina y cómo amar y lidiar con los desafíos. En el lado de la tecnología, he aprendido a adquirir información, lidiar con el estrés y pensar de manera lógica. Creo que este portafolio es el primer paso hacia un futuro transformador, unir pasión y carrera es el sueño de muchos y creo que puedo lograrlo."
    }
}


def get_string(idioma, key):
    return strings[idioma][key]
  
  
titulo = get_string(idioma,"titulo")
st.title(titulo)

st.subheader("Lincoln Sales e Gonçalves")

texto = get_string(idioma, "texto")
st.write(texto)
