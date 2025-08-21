import PyPDF2

pdf_file_path = "data/sampleresume.pdf"

try:
    with open(pdf_file_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
        print(text)
except FileNotFoundError:
    print(f"File not found: {pdf_file_path}")
except Exception as e:
    print(f"Error occurred: {e}")
