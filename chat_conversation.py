import streamlit as st 

message1 = st.chat_message("assistant")
message1.write("Hello this is assistant. How may I help you?")

message2 = st.chat_message("human")
message2.write("Hey I am human")



prompt = st.chat_input("Say something")
data : list = [] #we can also make it session variable so the state is maintained. Currently it acts as stateless
if prompt:
    data.append(prompt)
    st.write(f"User has sent the following prompt: {prompt}")

st.write(data)