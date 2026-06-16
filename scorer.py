skills_db = [
    "python",
    "sql",
    "power bi",
    "tensorflow",
    "pytorch",
    "scikit-learn",
    "machine learning",
    "ai",
    "agentic ai",
    "api",
    "n8n",
    "make.com",
    "automation",
    "data preprocessing",
    "aws",
    "azure",
    "docker",
    "kubernetes",
    "git",
    "github",
    "agile",
    "scrum",
    "uipath",
    "rpa"
]


def extract_skills(text):

    text = text.lower()

    found_skills = []

    for skill in skills_db:

        if skill.lower() in text:
            found_skills.append(skill)

    return found_skills


def calculate_ats_score(resume_skills, jd_skills):

    matched = set(resume_skills).intersection(set(jd_skills))

    if len(jd_skills) == 0:
        return 0

    score = (len(matched) / len(jd_skills)) * 100

    return round(score, 2)

def missing_skills(resume_skills, jd_skills):

    return list(
        set(jd_skills) - set(resume_skills)
    )