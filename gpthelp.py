import os
import openai

openai.api_key = "open-ai-key"

def get_gpt_suggestions(resume_keywords, job_description):
    prompt = f"""
    Resume Skills: {', '.join(resume_keywords)}
    Job Description: {job_description}

    Based on the job description, what skills or keywords are missing in the resume that are important?
    Provide a short, clear list of suggestions to improve the resume.
    """
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You're a helpful resume reviewer."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.5,
            max_tokens=150
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        return f"❌ GPT Error: {str(e)}"
