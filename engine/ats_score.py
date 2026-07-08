def calculate_ats_score(skills, missing_skills):

    total = len(skills) + len(missing_skills)

    if total == 0:
        return 0

    score = (len(skills) / total) * 100

    return round(score, 2)
def calculate_ats_score(skills, missing_skills):

    score = 50

    # skills bonus
    score += len(skills) * 5

    # missing skills penalty
    score -= len(missing_skills) * 3

    if score > 100:
        score = 100

    if score < 0:
        score = 0

    return score