# test_matcher.py
from gpthelp import get_gpt_suggestions

from resume_parser import extract_resume_text, extract_keywords
from job_scraper import get_sample_jobs
from matcher import get_match_scores

with open("sample_resume.pdf", "rb") as file:
    resume_text = extract_resume_text(file)
    keywords = extract_keywords(resume_text)

    jobs = get_sample_jobs()
    matches = get_match_scores(keywords, jobs)

    print("\n🔍 Top Job Matches:")
for job, score in matches:
    print(f"{job['title']} at {job['company']} — Match: {score}%")
    
    if score < 85:  # only suggest if match is low
        print("🤖 GPT Suggestions to improve resume:")
        suggestions = get_gpt_suggestions(keywords, job['description'])
        print(suggestions)

