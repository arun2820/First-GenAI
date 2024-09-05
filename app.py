from dotenv import load_dotenv
load_dotenv() # activate the local env variable

import streamlit as st
import os
import google.generativeai as genai

# setup the local environmnt for the google api key
genai.configure(api_key=os.getenv("GOOGLE-API-KEY"))

# GenAI Model
model = genai.GenerativeModel("gemini-pro")

#function to generate the content
def generate(question):
    response = model.generate_content(question)
    return(response.text)

#############STREAMLIT WEBPAGE ######################
st.set_page_config(page_title="LLM Q&A Application")
st.header('Generating Answers using Gemini pro')

#stramlit run app.py to rn the application
input  = st.text_input(label='Ask the Question',key='input')
submit = st.button(label='Generate Response')

if submit:
    response = generate(input)
    st.subheader('The response is:')
    st.write(response) 