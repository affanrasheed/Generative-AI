from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM
import streamlit as st


st.title("Llama3.1 app using LangChain")

template = """Question: {question} Answer: Let's think step by step."""

prompt = ChatPromptTemplate.from_template(template)

model = OllamaLLM(model="llama3.1")

chain = prompt | model

chain.invoke({"question":"What is LangChain?"})
question = st.chat_input("Enter your question here")
if question: 
    st.write(chain.invoke({"question": question}))
