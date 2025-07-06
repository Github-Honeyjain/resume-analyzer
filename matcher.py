# matcher.py
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def get_match_scores(resume_keywords, job_listings):
    resume_text = " ".join(resume_keywords)
    scores = []

    for job in job_listings:
        job_text = job["description"].lower()
        vectorizer = TfidfVectorizer().fit_transform([resume_text, job_text])
        score = cosine_similarity(vectorizer[0:1], vectorizer[1:2])[0][0]
        scores.append((job, round(score * 100, 2)))

    return sorted(scores, key=lambda x: x[1], reverse=True)
