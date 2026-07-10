def predict_career(skills):

    skills = [skill.lower() for skill in skills]

    if "python" in skills and "django" in skills:
        return "Backend Developer"

    elif "react" in skills or "javascript" in skills:
        return "Frontend Developer"

    elif "data science" in skills or "machine learning" in skills:
        return "Data Scientist"

    elif "python" in skills and "sql" in skills:
        return "Data Analyst"

    elif "python" in skills:
        return "Software Developer"

    else:
        return "Software Developer"