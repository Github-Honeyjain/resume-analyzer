import streamlit as st
from resume_parser import extract_resume_text, extract_keywords
from job_scraper import get_sample_jobs
from matcher import get_match_scores
from gpthelp import get_gpt_suggestions

# 📄 Set page config
st.set_page_config(
    page_title="🚀 Resume Analyzer & Job Matcher",
    layout="wide",
    page_icon="📄"
)

# 💻 CSS Styling
st.markdown("""
    <style>
    .main {
        background-color: #f5f7fa;
    }
    .stButton>button {
        color: white;
        background: linear-gradient(to right, #6a11cb, #2575fc);
        border: none;
        border-radius: 4px;
        padding: 0.5em 1em;
    }
    .stFileUploader {
        background-color: #ffffff;
        padding: 1em;
        border: 2px dashed #6a11cb;
        border-radius: 10px;
    }
    .stSpinner {
        color: #2575fc;
    }
    </style>
""", unsafe_allow_html=True)

# 🎯 Title & Instructions
st.title("🚀 Resume Analyzer & Job Matcher")
st.markdown("""
Upload your **resume** 📄 and let us:
- 🔍 Extract your **skills**
- 🎯 Match you with **jobs**
- 🤖 Suggest what to improve with GPT!

---
""")

uploaded_file = st.file_uploader("📤 Upload Your Resume (PDF only)", type=["pdf"])

if uploaded_file:
    try:
        with st.spinner("✨ Extracting resume content..."):
            resume_text = extract_resume_text(uploaded_file)

        if not resume_text.strip():
            st.error("❌ No text could be extracted. Please upload a valid text-based resume.")
        else:
            keywords = extract_keywords(resume_text)
            st.balloons()
            st.success("✅ Resume processed successfully!")

            # 🧠 Skills
            st.header("🧠 Extracted Skills")
            if keywords:
                st.markdown(f"""
                <div style="background-color:#e0f7fa;padding:10px;border-radius:5px;">
                {" | ".join(keywords)}
                </div>
                """, unsafe_allow_html=True)
            else:
                st.warning("No matching keywords found.")

            # 💼 Job Matches
            job_list = get_sample_jobs()
            matches = get_match_scores(keywords, job_list)

            st.header("💼 Top Job Matches")
            for job, score in matches:
                with st.expander(f"🎯 {job['title']} at {job['company']} — Match: {score}%"):
                    st.markdown(f"**📝 Description:** {job['description']}")
                    if score < 85:
                        with st.spinner("🤖 GPT Suggestions to improve your resume..."):
                            suggestions = get_gpt_suggestions(keywords, job["description"])
                            if "GPT Error" in suggestions:
                                st.warning(suggestions)
                            else:
                                st.markdown("**✨ Suggestions to Improve:**")
                                st.markdown(f"""
                                <div style="background-color:#fff3e0;padding:10px;border-radius:5px;">
                                {suggestions}
                                </div>
                                """, unsafe_allow_html=True)

    except Exception as e:
        st.error(f"🔥 An error occurred: {e}")
        import traceback
        st.text(traceback.format_exc())
else:
    st.info("⬆️ Please upload your resume above to begin.")
