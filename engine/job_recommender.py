job_data = {
    "backend developer": [
        "Backend Developer – TCS",
        "Python Developer – Infosys",
        "Django Developer – Wipro",
        "Software Engineer – Accenture",
        "Python Backend Engineer – Cognizant"
    ],

    "frontend developer": [
        "React Developer – HCL",
        "Frontend Engineer – Cognizant",
        "UI Developer – Tech Mahindra",
        "Web Developer – Infosys"
    ],

    "data scientist": [
        "Data Analyst – Deloitte",
        "Machine Learning Engineer – IBM",
        "Data Scientist – Capgemini",
        "AI Engineer – Accenture"
    ],

    "full stack developer": [
        "Full Stack Developer – TCS",
        "Software Engineer – Infosys",
        "MERN Stack Developer – Wipro",
        "Python Full Stack Developer – Cognizant"
    ],   # ✅ comma

    "data analyst": [
        "Data Analyst – Deloitte",
        "Business Analyst – EY",
        "SQL Developer – Infosys",
        "BI Analyst – Capgemini"
    ],

    "software developer": [
        "Software Developer – TCS",
        "Software Engineer – Infosys",
        "Associate Software Engineer – Accenture",
        "Programmer Analyst – Cognizant"
    ]
}


def recommend_jobs(career):
    if not career:
        return [
            "Software Engineer – TCS",
            "Python Developer – Infosys",
            "Web Developer – Wipro"
        ]

    return job_data.get(
        career.lower(),
        [
            "Software Engineer – TCS",
            "Python Developer – Infosys",
            "Web Developer – Wipro"
        ]
    )