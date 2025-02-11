import streamlit as st
from langchain_groq import ChatGroq

llm = ChatGroq(
    model="mixtral-8x7b-32768",
    temperature= 0,
    api_key="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",
)


st.title("simple llm Chatbot")
st.write("Enter your query below :")

user_input = st.text_input("your Question :","")

if st.button("Get Answer"):
    response = llm.invoke(user_input)
    st.write("### Response : ")
    st.write(response)