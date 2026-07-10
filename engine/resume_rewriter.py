def rewrite_resume(skills, missing_skills):

    resume = []

    resume.append("=== PROFESSIONAL SUMMARY ===")
    resume.append(
        "Motivated and detail-oriented software developer with knowledge of Python, web development, databases, and problem-solving. Passionate about building scalable applications and continuously learning new technologies."
    )

    if skills:
        resume.append("\n=== TECHNICAL SKILLS ===")
        resume.append(", ".join(skill.title() for skill in skills))

    if missing_skills:
        resume.append("\n=== RECOMMENDED SKILLS TO LEARN ===")
        resume.append(", ".join(skill.title() for skill in missing_skills))

    resume.append("\n=== PROJECT DESCRIPTION ===")
    resume.append(
        "Developed real-world web applications using Django, Python, HTML, CSS, JavaScript, SQL, and REST APIs. Implemented authentication, resume analysis, and database integration."
    )

    resume.append("\n=== STRENGTHS ===")
    resume.append("- Strong problem-solving skills")
    resume.append("- Quick learner")
    resume.append("- Team collaboration")
    resume.append("- Clean and maintainable coding practices")

    resume.append("\n=== CAREER OBJECTIVE ===")
    resume.append(
        "Seeking an opportunity as a Software Developer where I can apply my technical skills while contributing to organizational growth."
    )

    return resume