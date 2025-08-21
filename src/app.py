import streamlit as st
import os
import sys
from dotenv import load_dotenv
import io
import PyPDF2

from gemini_api import get_ai_response
from extractor import extract_text_from_pdf

# Load the env variables
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

# check for api_key
if not api_key:
    st.error("GOOGLE_API_KEY not found in environment variables.")
    sys.exit()

# StreamLit App
st.title("Resume Chatbot")
st.write("Upload a PDF resume to extract text and interact with the chatbot.")

# Chat Memory
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display the chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")
jobDescription = st.text_input("Enter the job description")

if uploaded_file is not None:
    try:
        extracted_text = extract_text_from_pdf(uploaded_file)
        st.success("PDF text extracted successfully.")

        user_input = st.text_input("Enter ur query")
        if st.button("Get Response"):
            if user_input and jobDescription:
                st.session_state.messages.append({"role" : "user" , "content" : user_input})
                with st.chat_message("user"):
                    st.markdown(user_input)

                st.info("Generating response...")
                response = get_ai_response(extracted_text, jobDescription, user_input)
                st.session_state.messages.append({"role" : "assistant" , "content" : response})
                with st.chat_message("assistant"):
                    st.markdown(response)

                # st.success("Response generated successfully.")
                # st.write(response)
            else:
                st.warning("Please enter both a job description and a query to get a response.")
    except Exception as e:
        st.error(f"Error occurred: {e}")
