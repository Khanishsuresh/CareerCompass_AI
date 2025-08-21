import streamlit as st
import google.generativeai as genai
import PyPDF2
import os
import sys
import io
from dotenv import load_dotenv

# Load the env variables
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

# check for api_key
if not api_key:
    st.error("GOOGLE_API_KEY not found in environment variables.")
    sys.exit()
else:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-1.5-flash")
    # st.success("Google API key configured successfully.")

# Get the response from the api model
def get_ai_response(extracted_text, job_description, user_query):
    try:
        prompt = f"""
        Given the extracted text from the resume and the job description:

        extracted_resume:{extracted_text}
        job description:{job_description}

        Based on this, perform the following operations:
        1. Provide a match score (from 0 to 100).
        2. List the top 5 skills from the resume that match the job description.
        3. Finally, answer the user's query: '{user_query}'

        Your response should be in a clear, formatted way.
        """
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"An error occurred: {e}"
    
# StreamLit App
st.title("Resume Chatbot")
st.write("Upload a PDF resume to extract text and interact with the chatbot.")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")
uploaded_jobDescription = st.text_input("Enter the job description")

if uploaded_file is not None:
    try:
        reader = PyPDF2.PdfReader(uploaded_file)
        extracted_text = ""
        for page in reader.pages:
            extracted_text += page.extract_text()
        st.success("PDF text extracted successfully.")

        user_input = st.text_input("Enter ur query")
        if st.button("Get Response"):
            if user_input:
                st.session_state.messages.append({"role" : "user" , "content" : user_input})
                with st.chat_message("user"):
                    st.markdown(user_input)

                st.info("Generating response...")
                response = get_ai_response(extracted_text, uploaded_jobDescription, user_input)
                st.session_state.messages.append({"role" : "assistant" , "content" : response})
                with st.chat_message("assistant"):
                    st.markdown(response)

                # st.success("Response generated successfully.")
                # st.write(response)
            else:
                st.warning("Please enter both a job description and a query to get a response.")
    except Exception as e:
        st.error(f"Error occurred: {e}")
