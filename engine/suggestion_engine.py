def generate_suggestions(skills, missing_skills):

    suggestions = []

    if len(skills) < 5:
        suggestions.append("Add more technical skills in resume")

    if "github" not in skills:
        suggestions.append("Add your GitHub profile link")

    if "project" not in skills:
        suggestions.append("Add projects section")

    if missing_skills:
        suggestions.append("Try learning: " + ", ".join(missing_skills))

    if "internship" not in skills:
        suggestions.append("Add internship or work experience")

    return suggestions