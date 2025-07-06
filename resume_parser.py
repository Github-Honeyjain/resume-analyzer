# resume_parser.py
import fitz  # PyMuPDF

def extract_resume_text(file):
    text = ""
    with fitz.open(stream=file.read(), filetype="pdf") as doc:
        for page in doc:
            text += page.get_text()
    return text

def extract_keywords(text):
    # Simple keyword matcher
    text = text.lower()
    skills = [
    "python", "java", "c++", "machine learning", "deep learning", "tensorflow", "keras",
    "data analysis", "sql", "mongodb", "numpy", "pandas", "nlp", "flask", "django",
    "java swing", "software development", "rest api", "html", "css", "javascript", "react"
]

    found = [skill for skill in skills if skill in text]
    return found
