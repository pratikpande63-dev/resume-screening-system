from resume_parser import extract_text_from_pdf
from scorer import extract_skills
from scorer import calculate_ats_score

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

print("\nResume Skills:")
print(resume_skills)

print("\nJD Skills:")
print(jd_skills)

print("\nATS Score:")
print(score)

from scorer import missing_skills

missing = missing_skills(
    resume_skills,
    jd_skills
)

print("\nMissing Skills:")
print(missing)