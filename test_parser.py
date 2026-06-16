# test_parser.py

from resume_parser import extract_text_from_pdf

resume_text = extract_text_from_pdf(
    "resumes/Pratik Pande.pdf"
)

jd_text = extract_text_from_pdf(
    "JD/jd.pdf"
)

print("===== RESUME =====")
print(resume_text[:500])

print("\n===== JOB DESCRIPTION =====")
print(jd_text[:500])