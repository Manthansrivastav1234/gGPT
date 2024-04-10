import cohere
import streamlit as st


co=cohere.Client('UsQYSzNIUqD7cOMVXvSNHg771GO866OvdgkDbp9e')

st.title("Manthan GPT")

if "messages" not in st.session_state:
     st.session_state["messages"]=[]

with st.sidebar:
     if st.button("DELETE THE HISTORY"):
          st.session_state.messages=[]

for message in st.session_state.messages:
     with st.chat_message(message['role']):
          st.markdown(message['text'])
if prompt:=st.chat_input("how may I Help You"):
     with st.chat_message("user"):
          st.markdown(prompt)
     response=co.chat(message=prompt,chat_history=st.session_state.messages)
     with st.chat_message("assisatnt"):
          st.markdown(response.text)
     st.session_state.messages.append({"role":"user","text":prompt})
     st.session_state.messages.append({"role":"assitant","text":response.text})
