from dotenv import load_dotenv
load_dotenv() # loading the environment variables

import streamlit as st
import os
import google.generativeai as genai

# functn to load the gemini model and get responses
model=genai.GenerativeModel("gemini-pro")
chat=model.start_chat(history=[])

def get_gemini_response(question):
    response = chat.send_message(question,stream=True)
    return response

# initialize the streamlit app
st.set_page_config(page_title="Q&A Demo")
st.header("Gemini LLM Application")

# initialize session state for chat history if it does not exist
if 'chat_history' not in st.session_state:
    st.session_state['chat_history']=[]


input=st.text_input("Input: ", key="input")
submit=st.button("Ask the question here")

if submit and input:
    response=get_gemini_response(input)
    # add user query and response to session history
    st.session_state['chat_history'].append(("You",input))
    st.subheader("The response is:")
    for chunk in response:
        st.write(chunk.text)
        st.session_state['chat_history'].append(("Bot",chunk.text))
st.subheader("The chat history is")

for role,text in st.session_state['chat_history']:
    st.write(f"{role}:{text}")