# Q&A Chatbot
import os
from langchain.llms import OpenAI 
from dotenv import load_dotenv
import streamlit as st


load_dotenv()    # take environment variables from .env.

# function to load OpenAI model and get responses
def get_openai_response(question):
    llm=OpenAI(openai_api_key=os.getenv("OPENAI_API_KEY"), model_name="gpt-3.5-turbo-instruct", temperature=0.5)
    response = llm(question)
    return response
    

# Intialize streamlit app
st.set_page_config(page_title="Q&A Demo")
st.header("Langchain Application")

input = st.text_input("Input: ", key="input")
response = get_openai_response(input)
submit = st.button("Ask the question")

## If ask is clicked
if submit:
    st.subheader("The Response is")
    st.write(response)
