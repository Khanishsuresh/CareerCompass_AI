import google.generativeai as genai
import os
import sys
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    print("GOOGLE_API_KEY not found in environment variables.")
    sys.exit()

extracted_text = """
Khanish Ram S
Coimbatore, Tamil Nadu, India    |   +91-8610947383   |   khanishsuresh@gmail.com   |  LinkedIn  |  GitHub
EDUCATION
Sri Eshwar College of Engineering
B. Tech. Computer Science and Business SystemsNov. 2022 - Present
CGPA: 8.24
EXPERIENCE
GIRL SCRIPT SUMMER OF CODE - 24 May 2024 - July 2024
Technical Skills: Data Structures and Algorithms, OOP, OS, Git, GitHub
Programming Languages: C++, Python, HTML, CSS, JavaScript (basic), SQL, Java (basic)
Web App Developer: React, SpringBoot, MySQL, MongoDB
Data Science: Data Analysis, Machine Learning (basic), Data Visualization (Matplotlib, Seaborn),
Power BI, Tableau, Web Scraping (basic)SKILLS
PROJECTS
EduTrack | React JS, Node.js, Express, MongoDB, Selenium, Gemini AI May 2024 - Present
Developed a full-stack pet adoption platform using Spring Boot for the backend and React for the
frontend. The application allows users to browse available pets, view details of animal shelters, and
submit adoption inquiries. The project features a RESTful API for managing pet, shelter, and user
data with a MySQL database.Role: Frontend developer  - Link
ACHIVEMENTS
Semifinalist in TechGIG - 2024 | Link
Participated in HackOn with AMAZON - season4  | Link
LeetCode: Max Rating - 1730| Problem Solved 530+  | Profile
CodeChef: Max Rating - 1750 | 3-Star Coder | Best Global Rank 127 | Problem Solved 800+ | Profile
Codeforces: Max Rating - 996  | Profile
HackerRank: 5-Star Java | 4-Star C | 4-Star Python | 3-Star C++  | Profile
GeeksforGeeks : Institute Rank 152 | Problem Solved - 30+  | Profile
CERTIFICATES
Mastering Data Structures & Algorithms using C and C++  | Udemy
Crash Course on Python  | Coursera
Power BI for Beginners  | Simplilearn
Intro to programming  | Kaggle
Data Science Foundations  | Great Learning
Data Science Training (V3 - Analytics)
» Completed a three-week data science training at V3 Analytics, focusing on Python for data analysis,
EDA, and linear regression modeling. Applied these techniques to analyze and model a given dataset.
July 2024 - Aug 2024
PYDS Internship (HubbleMind)
» Completed the PYDS Internship at Hubblemind, gaining practical experience in data science
through weekly project tasks, including data preprocessing, EDA, and model training.
Sep 2024 - Oct 2024
Contributed to open-source projects by fixing bugs, implementing features, and improving code quality.
Collaborated with mentors to deliver impactful solutions and enhance project efficiency.
TRAINING & INTERNSHIP
PetAdoption | React JS, SpringBoot, Java, MYSQL May 2025 - Present
Developed by a 4-member team, this project manages student details and integrates web scraping
for coding platform data. Using advanced generative AI, the admin section ensures efficient data
retrieval with intuitive prompts, enhancing frontend presentation and operational efficiencyRole: Backend developer  - Link
"""

try:
    genai.configure(api_key=api_key)

    model = genai.GenerativeModel("gemini-1.5-flash")
    user_query = "Summarize the resume content."
    prompt = f"Given the following text from a resume:\n\n---\n{extracted_text}\n---\n\nAnswer the following question based ONLY on the provided text: '{user_query}'"
    response = model.generate_content(prompt)
    print(response.text)

except Exception as e:
    print(f"An error occurred: {e}")
    print("Error occurred while processing the extracted text.")
