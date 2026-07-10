def get_resume_tips(missing_skills):

    tips = []

    for skill in missing_skills:

        tips.append(f"Learn {skill} and add a project related to it in your resume.")

    tips.append("Add GitHub project links in your resume.")
    tips.append("Keep resume length 1 page.")
    tips.append("Use action words like Developed, Built, Created.")
    tips.append("Add internship or project experience.")

    return tips