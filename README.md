# CareerCompass AI

This project is a conversational AI chatbot that helps users analyze and compare their resume against a job description. By leveraging AI, it provides a compatibility score and lists key skills from the resume that match the job requirements, offering valuable insights for job seekers.

## Features

* **Resume Analysis:** Extracts and analyzes text from PDF resumes.
* **Job Description Matching:** Compares a resume against a user-provided job description.
* **Match Score:** Provides a percentage-based compatibility score to show how well a resume aligns with a job description.
* **Skills Analysis:** Identifies and lists the top skills from the resume that match the job description.
* **Conversational Interface:** An interactive chat interface allows users to ask follow-up questions about the analysis.
* **Conversation Memory:** Maintains the chat history to provide context for subsequent queries.

## Tech Stack

* **Programming Language:** Python
* **Web Framework:** Streamlit
* **AI Model:** Gemini-1.5-Flash
* **Libraries:**
    * `PyPDF2`: For PDF text extraction.
    * `google-generativeai`: To interact with the Gemini API.
    * `python-dotenv`: For managing environment variables securely.
    * `re`: For parsing the AI's response.

## Folder Structure

```bash
CareerCompass_AI/
├── .gitignore
├── .env
├── requirements.txt
├── data/
│   └── sampleresume.pdf
└── src/
    ├── app.py           # Main Streamlit app and UI
    ├── gemini_api.py    # Gemini API interaction logic
    ├── extractor.py     # PDF and text extraction logic
    └── utils.py         # Helper functions
```


## Setup and Installation

Follow these steps to set up and run the project locally.

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/khanishsuresh/careercompass_ai.git
    cd careercompass_ai
    ```

2.  **Create a virtual environment:**
    ```bash
    python -m venv venv
    ```

3.  **Activate the virtual environment:**
    * **On Windows:**
        ```bash
        venv\Scripts\activate
        ```
    * **On macOS/Linux:**
        ```bash
        source venv/bin/activate
        ```

4.  **Install the required libraries:**
    ```bash
    pip install -r requirements.txt
    ```

5.  **Set up your Gemini API key:**
    * Create a `.env` file in the main project directory.
    * Add your Gemini API key to the file in the following format:
        ```
        GOOGLE_API_KEY="your_api_key_here"
        ```

6.  **Run the Streamlit app:**
    ```bash
    streamlit run src/app.py
    ```
    The application will open in your web browser. You can now upload a resume, enter a job description, and interact with the chatbot.
