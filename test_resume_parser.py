# test_resume_parser.py
from resume_parser import extract_resume_text, extract_keywords

with open("sample_resume.pdf", "rb") as file:
    resume_text = extract_resume_text(file)
    print("Extracted Text:\n", resume_text)

    keywords = extract_keywords(resume_text)
    print("\nDetected Skills:\n", keywords)
