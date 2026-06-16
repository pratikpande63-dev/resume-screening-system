import ollama

def analyze_resume(resume_text, jd_text, ats_score):

    prompt = f"""
You are an ATS Resume Screening Expert.

Resume:
{resume_text}

Job Description:
{jd_text}

Current ATS Score:
{ats_score}

Provide:

1. ATS Score Review
2. Strengths
3. Weaknesses
4. Missing Skills
5. Interview Chances
6. Suggestions to Improve Resume

Give the response in clean bullet points.
"""

    response = ollama.chat(
        model="llama3.2",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]