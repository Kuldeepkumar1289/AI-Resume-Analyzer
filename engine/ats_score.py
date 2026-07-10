def calculate_ats_score(skills, missing_skills):
    """
    Calculates the ATS score based on detected skills and missing career gap skills.
    Starts with a baseline score of 50, adds bonuses for present skills, 
    and applies penalties for missing prerequisites.
    """
    score = 50

    # Add bonus for each detected skill
    score += len(skills) * 5

    # Apply penalty for each missing professional skill
    score -= len(missing_skills) * 3

    # Ensure score boundaries remain strictly between 0 and 100
    if score > 100:
        score = 100
    if score < 0:
        score = 0

    return score