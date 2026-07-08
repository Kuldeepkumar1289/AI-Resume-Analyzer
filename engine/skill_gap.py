def find_missing_skills(career, skills):

    career_skills = {
        "Data Scientist": ["python", "machine learning", "pandas", "numpy", "sql"],
        "Web Developer": ["html", "css", "javascript", "django", "react"],
        "Backend Developer": ["python", "django", "sql", "api", "git"],
        "AI Engineer": ["python", "machine learning", "deep learning", "tensorflow"],
    }

    required = career_skills.get(career, [])

    missing = []

    for skill in required:
        if skill not in skills:
            missing.append(skill)

    return missing