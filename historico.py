import streamlit as st

if "historico" not in st.session_state:
    st.session_state.historico = novo_historico()

for mensagem in st.session_state.historico:
    if mensagem["role"] == "system":
        continue
    with st.chat_message(mensagem["role"]):
        st.markdown(mensagem["content"])

pergunta = st.chat_input("Digite...")
if pergunta:
 st.session_state.historico.append({"role": "user", "content": pergunta})
