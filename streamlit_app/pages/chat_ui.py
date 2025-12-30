import streamlit as st
from app.core.llm_client import LLMClient
from app.services.chat_service import ChatService

st.title("🏈 TrojanChat")

if "history" not in st.session_state:
    st.session_state.history = ""

llm = LLMClient(api_key=st.secrets["OPENAI_API_KEY"])
chat = ChatService(llm)

user_input = st.text_input("Ask about USC football")

if user_input:
    response = chat.respond(st.session_state.history, user_input)
    st.session_state.history += f"\nUser: {user_input}\nBot: {response}"
    st.write(response)