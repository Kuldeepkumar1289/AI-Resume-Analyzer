def detect_skills(text):

    skills_db = [
        "python",
        "java",
        "c++",
        "django",
        "flask",
        "sql",
        "mysql",
        "machine learning",
        "data science",
        "html",
        "css",
        "javascript",
        "react",
        "node",
        "git"
    ]

    found_skills = []

    text = text.lower()

    for skill in skills_db:
        if skill in text:
            found_skills.append(skill)

    return found_skills