def match_resume_with_job(skills, job_description):

    if not job_description:
        return {
            "score": 0,
            "matched_skills": [],
            "missing_skills": []
        }

    job_description = job_description.lower()

    matched_skills = []
    missing_skills = []

    for skill in skills:
        if skill.lower() in job_description:
            matched_skills.append(skill)
        else:
            missing_skills.append(skill)

    if len(skills) == 0:
        score = 0
    else:
        score = (len(matched_skills) / len(skills)) * 100

    return {
        "score": round(score, 2),
        "matched_skills": matched_skills,
        "missing_skills": missing_skills
    }