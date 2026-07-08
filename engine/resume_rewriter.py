def rewrite_resume(skills, missing_skills):

    improved = []

    # Skills section improve
    if skills:
        improved.append("✅ Skills Section:")
        improved.append("Proficient in " + ", ".join(skills))

    # Add missing skills suggestion
    if missing_skills:
        improved.append("\n📌 Add these skills to improve profile:")
        improved.append(", ".join(missing_skills))

    # Experience section suggestion
    improved.append("\n💼 Experience सुझाव:")
    improved.append("Developed projects using modern technologies and improved performance.")

    # Achievement suggestion
    improved.append("\n🏆 Achievements:")
    improved.append("Increased efficiency by 30% through optimized code.")

    # Project suggestion
    improved.append("\n🚀 Projects:")
    improved.append("Built real-world applications using Django, APIs, and databases.")

    return improved