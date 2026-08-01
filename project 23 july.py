#inncluding packages
from langchain_community.llms import Ollama 
import streamlit as st 
from langchain_core. prompts import ChatPromptTemplate 
from langchain_core.output_parsers import StrOutputParser 

#creating prompts 
prompt = ChatPromptTemplate. from_messages(
    [
        ("system","You are helpful assistant. please respond to the question asked "),
        ("user","Question:{question}")
    ]
) 

#frontend UI  Design using Streamlit framework 
st.title("M GPT")
input_text = st.text_input("Ask your question")

# Ollama model integration 
llm = Ollama(model="gemma2:latest")# step1 
output_parser = StrOutputParser()# step2
chain = prompt | llm | output_parser 

#input validation 
if input_text:
    st.write(chain.invoke({"question": input_text}))
    