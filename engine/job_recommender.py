job_data = {

    "Backend Developer": [
        "Backend Developer – TCS",
        "Python Developer – Infosys",
        "Django Developer – Wipro",
        "Software Engineer – Accenture"
    ],

    "Data Scientist": [
        "Data Analyst – Deloitte",
        "Machine Learning Engineer – IBM",
        "Data Scientist – Capgemini"
    ],

    "Frontend Developer": [
        "React Developer – HCL",
        "Frontend Engineer – Cognizant",
        "UI Developer – Tech Mahindra"
    ]

}


def recommend_jobs(career):

    return job_data.get(career, [])