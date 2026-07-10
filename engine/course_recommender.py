def recommend_courses(missing_skills):

    course_map = {
        "python": {
            "title": "Python for Everybody",
            "link": "https://www.coursera.org/learn/python"
        },

        "java": {
            "title": "Java Programming Masterclass",
            "link": "https://www.udemy.com/course/java-programming"
        },

        "django": {
            "title": "Django Full Course",
            "link": "https://www.youtube.com/results?search_query=django+full+course"
        },

        "react": {
            "title": "React Course",
            "link": "https://www.freecodecamp.org/learn/front-end-development-libraries/react/"
        },

        "javascript": {
            "title": "JavaScript Course",
            "link": "https://javascript.info/"
        },

        "html": {
            "title": "HTML Course",
            "link": "https://www.w3schools.com/html/"
        },

        "css": {
            "title": "CSS Course",
            "link": "https://www.w3schools.com/css/"
        },

        "sql": {
            "title": "SQL Course",
            "link": "https://www.w3schools.com/sql/"
        },

        "mysql": {
            "title": "MySQL Tutorial",
            "link": "https://www.w3schools.com/mysql/"
        },

        "git": {
            "title": "Git & GitHub",
            "link": "https://www.freecodecamp.org/news/git-and-github-for-beginners/"
        },

        "data science": {
            "title": "IBM Data Science",
            "link": "https://www.coursera.org/professional-certificates/ibm-data-science"
        }
    }

    courses = []

    for skill in missing_skills:
        skill = skill.lower()

        if skill in course_map:
            courses.append({
                "skill": skill.title(),
                "title": course_map[skill]["title"],
                "course": course_map[skill]["link"]
            })

    return courses