from resume_parser import extract_text_from_pdf
from scorer import extract_skills
from scorer import calculate_ats_score
from llm_analyzer import analyze_resume

resume_text = extract_text_from_pdf(
    "resumes/Pratik Pande.pdf"
)

jd_text = extract_text_from_pdf(
    "JD/jd.pdf"
)

resume_skills = extract_skills(resume_text)
jd_skills = extract_skills(jd_text)

score = calculate_ats_score(
    resume_skills,
    jd_skills
)

analysis = analyze_resume(
    resume_text,
    jd_text,
    score
)

print("\nATS Score:", score)
print("\n")
print(analysis)