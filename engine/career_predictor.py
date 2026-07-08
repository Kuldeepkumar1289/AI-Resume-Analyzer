def predict_career(skills):

    if "django" in skills or "html" in skills:
        return "Backend Developer"

    elif "data science" in skills or "machine learning" in skills:
        return "Data Scientist"

    elif "sql" in skills and "python" in skills:
        return "Data Analyst"

    else:
        return "Software Developer"