import streamlit as st
from transformers import pipeline

model = pipeline("text-generation", model="openai-gpt")
input_text = st.text_area("Enter Text", height=100)
generate_button = st.button("Generate Text")
if generate_button:
    if input_text:
        output_text = model(input_text)[0]["generated_text"]
        st.markdown("<div>"+output_text+"</div>", unsafe_allow_html=True)
