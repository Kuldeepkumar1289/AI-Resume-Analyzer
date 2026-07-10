def generate_feedback(skills, missing_skills, ats_score):

    feedback = []

    # Weakness
    if missing_skills:
        feedback.append("❌ You are missing important skills: " + ", ".join(missing_skills))

    # Strength
    if skills:
        feedback.append("✅ You have strong skills in: " + ", ".join(skills))

    # ATS improvement
    if ats_score < 50:
        feedback.append("⚠️ Your resume ATS score is low. Improve formatting and add keywords.")
    elif ats_score < 75:
        feedback.append("👍 Your resume is decent but can be improved.")
    else:
        feedback.append("🔥 Your resume is strong and ATS optimized!")

    # General tips
    feedback.append("📌 Add projects and real-world experience.")
    feedback.append("📌 Include GitHub links.")
    feedback.append("📌 Use measurable achievements (e.g., improved performance by 30%)")

    return feedback