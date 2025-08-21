import google.generativeai as genai
import os
import sys
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    # Handled in main app
    pass
else:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-1.5-flash")

def get_ai_response(extracted_text , job_description , user_query):
    """
    Generates a response from the Gemini API based on the resume and job description.
    """
    try:
        if not extracted_text or not user_query:
            return "Please provide the resume and the query first"
        
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
        return f"An error occured during processing the API request: {e}"