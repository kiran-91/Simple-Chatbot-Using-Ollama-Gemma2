import os 
from dotenv import load_dotenv
from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st 

load_dotenv()
# for langchain and langsmith tracking 
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACKING_V2"]="true"


# prompt template 
prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant. Please respond to the question asked"),
        ("user","Question: {Question}")   
    ]
)

# streamlit app 

st.title("Chatbot using Ollama and Llama 3.2")
input_text=st.text_input("What question do you have in mind")


llm=Ollama(model="gemma2:2b")
output_parser=StrOutputParser()

chain=prompt|llm|output_parser

if input_text:
    try:
        response=chain.invoke({"Question":input_text})
        st.write(response)
    except Exception as e:
        st.error(f"An error occured: {e}")