import streamlit as st
import google.generativeai as genai

# Title
st.set_page_config(page_title="Gemini Chatbot", layout="centered")
st.title("Gemini Chatbot (Free via API)")

# Set API key
genai.configure(api_key=st.secrets["gemini_api_key"])

# Load Gemini model
model = genai.GenerativeModel("gemini-pro")

# Session state
if "history" not in st.session_state:
    st.session_state.history = []

# Input from user
user_input = st.text_input("You:", placeholder="Ask anything...")

# Chat logic
if user_input:
    st.session_state.history.append(("user", user_input))
    with st.spinner("Gemini is thinking..."):
        response = model.generate_content(user_input)
        bot_reply = response.text
        st.session_state.history.append(("bot", bot_reply))
        st.markdown(f"**Bot:** {bot_reply}")

# Display chat history
for role, text in reversed(st.session_state.history):
    if role == "user":
        st.markdown(f"**You:** {text}")
    else:
        st.markdown(f"**Gemini:** {text}")
