## Integrate our code OpenAI API
import os
from constants import openai_key
from langchain_community.llms import OpenAI
from langchain import PromptTemplate
from langchain.chains import LLMChain, SequentialChain

import streamlit as st

os.environ["OPENAI_API_KEY"] = openai_key

# streamlit framework
st.title('Celebrity Search Results')
input_text = st.text_input("Search the topic you want")

# Prompt Templates
first_input_prompt = PromptTemplate(
    input_variable=['name'],
    template="Tell me about celebrity {name}"
)

## OPENAI LLMs 
llm = OpenAI(temperature=0.8)
chain = LLMChain(llm=llm, prompt=first_input_prompt, verbose=True, output_key='person')

# Prompt Templates
second_input_prompt = PromptTemplate(
    input_variable=['person'],
    template="When was {person} born"
)
chain2 = LLMChain(llm=llm, prompt=second_input_prompt, verbose=True, output_key='dob')


third_input_prompt = PromptTemplate(
    input_variable=['dob'],
    template="Mention 5 major events happened around {dob} in the world"
)
chain3 = LLMChain(llm=llm, prompt=third_input_prompt, verbose=True, output_key='description')


parent_chain = SequentialChain(chains=[chain, chain2, chain3], input_variables=['name'], output_variables=['person', 'dob', 'description'], verbose=True)


if input_text:
    st.write(parent_chain({'name': input_text}))
