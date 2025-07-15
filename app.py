import streamlit as st
from utils.pdf_reader import extract_text_from_pdf
from utils.text_preprocessor import preprocess_text
from utils.skill_extractor import extract_skills
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from utils.match_score import get_match_score  # if in separate file
from utils.improvement_tips import generate_improvement_tips
from utils.report_generator import generate_report
import io
from utils.report_generation import generate_pdf_report

st.title("📄 Resume vs Job Description Analyzer")

st.subheader("Upload Resume (PDF or TXT)")
resume_file = st.file_uploader("Choose your Resume", type=["pdf", "txt"])

st.subheader("Upload Job Description (PDF or TXT)")
jd_file = st.file_uploader("Choose Job Description", type=["pdf", "txt"])

if resume_file and jd_file:
    # 1. Extract text
    resume_text = extract_text_from_pdf(resume_file)
    jd_text = extract_text_from_pdf(jd_file)

    # 2. Preprocess text
    resume_tokens = preprocess_text(resume_text)
    jd_tokens = preprocess_text(jd_text)

    # 3. Extract skills
    resume_skills = extract_skills(resume_tokens)
    jd_skills = extract_skills(jd_tokens)

    # 4. Show extracted skills
    st.markdown("### ✅ Extracted Resume Skills:")
    st.write(resume_skills)

    st.markdown("### 📌 Extracted JD Required Skills:")
    st.write(jd_skills)

    # 5. Similarity scoring
    match_score = get_match_score(resume_text, jd_text)
    st.markdown(f"### 📊 Match Score: `{match_score}%`")

    # 6. Missing skills (optional)
    missing_skills = jd_skills - resume_skills
    if missing_skills:
        st.markdown("### ❌ Missing Skills:")
        st.write(sorted(missing_skills))

        # 💡 Add tips here
        tips = generate_improvement_tips(missing_skills)
        st.markdown("### 💡 Suggested Improvements:")
        for tip in tips:
            st.markdown(f"- {tip}")

        # Generate report string
        report_text = generate_report(match_score, resume_skills, jd_skills, missing_skills, tips)

        # Convert to file-like object
        report_bytes = io.BytesIO()
        report_bytes.write(report_text.encode())
        report_bytes.seek(0)

        # Download button
        st.markdown("### 📥 Download Your Report:")
        st.download_button(
            label="📥 Download Report as TXT",
            data=report_bytes,
            file_name="resume_vs_jd_report.txt",
            mime="text/plain"
        )

        # PDF Report
        pdf_bytes = generate_pdf_report(match_score, resume_skills, jd_skills, missing_skills, tips)

        st.download_button(
            label="📥 Download Report as PDF",
            data=pdf_bytes,
            file_name="resume_vs_jd_report.pdf",
            mime="application/pdf"
        )

    else:
        st.markdown("✅ Great! All JD skills are covered in the resume.")

    # 7. Text preview
    with st.expander("📜 Extracted Resume Text"):
        st.write(resume_text[:1000])

    with st.expander("📝 Extracted JD Text"):
        st.write(jd_text[:1000])
