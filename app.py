import streamlit as st

from resume_parser import extract_text_from_pdf
from scorer import extract_skills
from scorer import calculate_ats_score
from scorer import missing_skills

from llm_analyzer import analyze_resume


st.title("AI Resume Screening System")

st.write("Upload Resume PDF and Job Description PDF")


resume_file = st.file_uploader(
    "Upload Resume",
    type=["pdf"]
)

jd_file = st.file_uploader(
    "Upload Job Description",
    type=["pdf"]
)


if st.button("Analyze Resume"):

    if resume_file and jd_file:

        with open("temp_resume.pdf", "wb") as f:
            f.write(resume_file.getbuffer())

        with open("temp_jd.pdf", "wb") as f:
            f.write(jd_file.getbuffer())

        resume_text = extract_text_from_pdf(
            "temp_resume.pdf"
        )

        jd_text = extract_text_from_pdf(
            "temp_jd.pdf"
        )

        resume_skills = extract_skills(
            resume_text
        )

        jd_skills = extract_skills(
            jd_text
        )

        score = calculate_ats_score(
            resume_skills,
            jd_skills
        )

        missing = missing_skills(
            resume_skills,
            jd_skills
        )

        analysis = analyze_resume(
            resume_text,
            jd_text,
            score
        )

        st.success("Analysis Complete")

        st.subheader("ATS Score")
        st.metric("Score", f"{score}%")

        st.subheader("Resume Skills")
        st.write(resume_skills)

        st.subheader("JD Skills")
        st.write(jd_skills)

        st.subheader("Missing Skills")
        st.write(missing)

        st.subheader("AI Analysis")
        st.write(analysis)

    else:
        st.warning("Please upload both PDFs")