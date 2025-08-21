import PyPDF2
import io

def extract_text_from_pdf(uploaded_resume):
    """
    Extracts all text from a PDF file uploaded to Streamlit.
    """
    try:
        pdf_reader = PyPDF2.PdfReader(uploaded_resume)
        extracted_text = ""
        for page in pdf_reader.pages:
            extracted_text += page.extract_text()
        return extracted_text
    except Exception as e:
        raise Exception (f"An error occured in extracting text from PDF: {e}")
