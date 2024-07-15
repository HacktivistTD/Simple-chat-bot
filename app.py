import google.generativeai as genai
from dotenv import load_dotenv
import os
import streamlit as st

# ... rest of your code

def list_available_models():
    models = genai.list_models()
    for model in models:
        st.write(model.name, model.supported_methods)

def main():
    """Displays the chatbot interface and handles user input."""
    st.title("Generative Language Chatbot")

    # List available models
    list_available_models()

    # ... rest of your code
