#Titulo 
#input ao chat (campo de mensagem)
# a cada mensagem que usuario enviar:
    # mostrar a mensagem que usuario enviou no chat
    # pegar a pergunta e enviar pra uma IA responder
    # exibir a resposta da IA na tela
    
#a IA que será usada: OpenAI

#Iniciando o programa


import streamlit as st
from openai import OpenAI
import os


#Style
st.set_page_config(
    page_title="Chatbot IA",
    page_icon="🤖",
    layout="wide"
)

st.markdown(
    """
    <div class="title-container">
        <h1>🤖 Chatbot Inteligente</h1>
        <p>Assistente virtual com IA</p>
    </div>
    """,
    unsafe_allow_html=True
)

#chave da API OpenAI
modelo_ia = OpenAI(api_key="")

st.write("# Chatbot IA")#markdown

if not "lista_mensagens" in st.session_state:
    st.session_state["lista_mensagens"] =[]


texto_usario = st.chat_input("Qual é a sua dúvida?")

for mensagem in st.session_state["lista_mensagens"]:
    role = mensagem ["role"]
    content = mensagem ["content"]
    st.chat_message(role).write(content)

if texto_usario:
    st.chat_message("user").write(texto_usario)
    mensagen_usuario = {"role":"user","content":texto_usario}
    st.session_state["lista_mensagens"].append(mensagen_usuario)
    #Nome
    #user
    #assistant
    
    #IA respondeu
    resposta_ia = modelo_ia.chat.completions.create(
        messages= st.session_state["lista_mensagens"],
        model="gpt-4o",
        )
    
    texto_resposta_ia = resposta_ia.choices[0].message.content

    st.chat_message("assistant").write(texto_resposta_ia)
    mensagem_ia = {"role":"assistant", "content":texto_resposta_ia }
    st.session_state["lista_mensagens"].append(mensagem_ia)

 



    
                             

