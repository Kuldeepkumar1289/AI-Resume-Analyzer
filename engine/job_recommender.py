# engine/job_recommender.py


job_data = {

    "backend developer": [

        {
            "title": "Backend Developer",
            "company": "TCS",
            "skills": [
                "Python",
                "Django",
                "REST API",
                "SQL"
            ]
        },

        {
            "title": "Python Developer",
            "company": "Infosys",
            "skills": [
                "Python",
                "Django",
                "SQL"
            ]
        },

        {
            "title": "Django Developer",
            "company": "Wipro",
            "skills": [
                "Python",
                "Django",
                "REST API"
            ]
        },

        {
            "title": "Software Engineer",
            "company": "Accenture",
            "skills": [
                "Python",
                "SQL",
                "Git"
            ]
        },

        {
            "title": "Python Backend Engineer",
            "company": "Cognizant",
            "skills": [
                "Python",
                "Django",
                "REST API",
                "SQL"
            ]
        }

    ],


    "frontend developer": [

        {
            "title": "React Developer",
            "company": "HCL",
            "skills": [
                "HTML",
                "CSS",
                "JavaScript",
                "React"
            ]
        },

        {
            "title": "Frontend Engineer",
            "company": "Cognizant",
            "skills": [
                "JavaScript",
                "React",
                "HTML",
                "CSS"
            ]
        },

        {
            "title": "UI Developer",
            "company": "Tech Mahindra",
            "skills": [
                "HTML",
                "CSS",
                "JavaScript"
            ]
        },

        {
            "title": "Web Developer",
            "company": "Infosys",
            "skills": [
                "HTML",
                "CSS",
                "JavaScript"
            ]
        }

    ],


    "data scientist": [

        {
            "title": "Data Scientist",
            "company": "Capgemini",
            "skills": [
                "Python",
                "Machine Learning",
                "SQL"
            ]
        },

        {
            "title": "Machine Learning Engineer",
            "company": "IBM",
            "skills": [
                "Python",
                "Machine Learning",
                "Data Science"
            ]
        },

        {
            "title": "AI Engineer",
            "company": "Accenture",
            "skills": [
                "Python",
                "Machine Learning",
                "Artificial Intelligence"
            ]
        }

    ],


    "full stack developer": [

        {
            "title": "Full Stack Developer",
            "company": "TCS",
            "skills": [
                "HTML",
                "CSS",
                "JavaScript",
                "React",
                "Python",
                "Django"
            ]
        },

        {
            "title": "Software Engineer",
            "company": "Infosys",
            "skills": [
                "JavaScript",
                "React",
                "Python",
                "SQL"
            ]
        },

        {
            "title": "Python Full Stack Developer",
            "company": "Cognizant",
            "skills": [
                "Python",
                "Django",
                "React",
                "SQL"
            ]
        },

        {
            "title": "MERN Stack Developer",
            "company": "Wipro",
            "skills": [
                "MongoDB",
                "Express",
                "React",
                "Node.js"
            ]
        }

    ],


    "data analyst": [

        {
            "title": "Data Analyst",
            "company": "Deloitte",
            "skills": [
                "SQL",
                "Excel",
                "Python",
                "Data Analysis"
            ]
        },

        {
            "title": "Business Analyst",
            "company": "EY",
            "skills": [
                "SQL",
                "Data Analysis",
                "Excel"
            ]
        },

        {
            "title": "BI Analyst",
            "company": "Capgemini",
            "skills": [
                "SQL",
                "Data Visualization",
                "Power BI"
            ]
        }

    ],


    "software developer": [

        {
            "title": "Software Developer",
            "company": "TCS",
            "skills": [
                "Programming",
                "SQL",
                "Git"
            ]
        },

        {
            "title": "Software Engineer",
            "company": "Infosys",
            "skills": [
                "Programming",
                "SQL",
                "Problem Solving"
            ]
        },

        {
            "title": "Associate Software Engineer",
            "company": "Accenture",
            "skills": [
                "Programming",
                "Git",
                "SQL"
            ]
        },

        {
            "title": "Programmer Analyst",
            "company": "Cognizant",
            "skills": [
                "Programming",
                "SQL",
                "Problem Solving"
            ]
        }

    ]

}


def recommend_jobs(career):

    if not career:

        return [

            {
                "title": "Software Engineer",
                "company": "TCS",
                "skills": [
                    "Programming",
                    "SQL",
                    "Git"
                ]
            }

        ]

    career = career.lower().strip()

    return job_data.get(

        career,

        [

            {
                "title": "Software Engineer",
                "company": "TCS",
                "skills": [
                    "Programming",
                    "SQL",
                    "Git"
                ]
            },

            {
                "title": "Software Developer",
                "company": "Infosys",
                "skills": [
                    "Programming",
                    "SQL"
                ]
            }

        ]

    )