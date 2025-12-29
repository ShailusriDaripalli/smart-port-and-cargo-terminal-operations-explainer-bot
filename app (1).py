import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Gemini API
genai.configure(api_key=os.getenv("AIzaSyCDkLkZ8rhR1AKbKU1Bzn9FkBHYkbFZXWo"))

# Create Gemini Flash model
model = genai.GenerativeModel(
    model_name="models/gemini-3-flash-preview",
    system_instruction="""
You are a Smart Port & Cargo Terminal Operations Explainer Bot.

Your role:
- Explain port operations, container handling, customs processes, and yard management.
- Provide educational and training-level explanations only.

Restrictions:
- DO NOT schedule vessels.
- DO NOT approve cargo clearance.
- DO NOT generate invoices or billing actions.
- DO NOT perform operational decisions.

If asked for restricted actions, politely refuse and provide only general information.

Always keep responses simple, structured, and industry-focused.
"""
)

# Streamlit UI
st.set_page_config(page_title="Smart Port Ops Explainer Bot", layout="centered")
st.title("⚓ Smart Port & Cargo Terminal Operations Bot")
st.write("AI-powered explanation system for port & maritime logistics")

# Chat session
if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(history=[])

# Input
user_input = st.chat_input("Ask about port or cargo terminal operations...")

if user_input:
    with st.chat_message("user"):
        st.write(user_input)

    response = st.session_state.chat.send_message(user_input)

    with st.chat_message("assistant"):
        st.write(response.text)

