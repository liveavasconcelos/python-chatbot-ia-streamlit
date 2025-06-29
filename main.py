# titulo
# input do chat
# a cada mensagem enviada:
    # mostrar a mensagem enviada pelo usuario
    # enviar a mensagem do usuario para a IA responder
    # aparece na tela a mensagem da IA

# streamlit - frintend e backend
# opcoes mais robustas: flash, django, fastapi
import streamlit as st
from openai import OpenAI

modelo = OpenAI(api_key="cole a chave da API aqui")

st.write("ChatBot com IA") #markdown

# session_state
if not "lista_mensagens" in st.session_state:
    st.session_state["lista_mensagens"] = []

# para adicionar uma mensagem: st.session_state["lista_mensagens"].append(mensagem)


#exibir o histórico de mensagens
for mensagem in st.session_state["lista_mensagens"]:
    role = mensagem["role"]
    content = mensagem["content"]
    st.chat_message(role).write(content)


mensagem_usuario = st.chat_input("Escreva sua mensagem aqui..")

if mensagem_usuario:
    print(mensagem_usuario)
    st.chat_message("user").write(mensagem_usuario) #balãozinho com mensagem do usuario
    mensagem = {"role": "user", "content": mensagem_usuario}
    st.session_state["lista_mensagens"]

    # resposta da IA
    resposta_modelo = modelo.chat.completions.create(
        messages = st.session_state["lista_mensagens"],
        model = "gpt-4o"
    )
    resposta_ia = resposta_modelo.choices[0].message.content

    #exibir a resposta da IA na tela 
    st.chat_message("assistant").write("Certo!")
    mensagem_ia = {"role": "assistant", "content": resposta_ia}
    st.session_state["lista_mensagens"].append(mensagem_ia)

