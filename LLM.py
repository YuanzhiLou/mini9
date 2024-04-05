import streamlit as st
from transformers import pipeline

model = pipeline("text-generation", model="openai-gpt")

input_text = st.text_input("Enter some text")
generate_button = st.button("Generate")

if generate_button:
    output_text = model(input_text)[0]["generated_text"]
    st.text(output_text)
