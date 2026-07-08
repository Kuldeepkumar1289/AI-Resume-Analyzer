roadmaps = {

    "Backend Developer": [
        "Learn Python deeply",
        "Master Django",
        "Learn REST API",
        "Learn Docker",
        "Learn AWS",
        "Build 3 Backend Projects"
    ],

    "Data Scientist": [
        "Learn Python",
        "Learn Pandas and NumPy",
        "Learn Data Visualization",
        "Learn Machine Learning",
        "Work on datasets",
        "Build ML projects"
    ],

    "Frontend Developer": [
        "Learn HTML CSS",
        "Learn JavaScript",
        "Learn React",
        "Learn UI/UX basics",
        "Build 3 frontend projects"
    ]
}

def generate_roadmap(career):

    return roadmaps.get(career, [])