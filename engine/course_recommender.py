# engine/course_recommender.py

COURSE_LINKS = {

    "python": {
        "course": "https://www.freecodecamp.org/learn/scientific-computing-with-python/",
        "reason": "Improve Python programming fundamentals and problem-solving."
    },

    "java": {
        "course": "https://www.freecodecamp.org/learn/java/",
        "reason": "Learn Java programming and object-oriented programming."
    },

    "sql": {
        "course": "https://www.w3schools.com/sql/",
        "reason": "Learn database queries and SQL fundamentals."
    },

    "mysql": {
        "course": "https://www.mysql.com/doc/",
        "reason": "Understand MySQL databases and database management."
    },

    "javascript": {
        "course": "https://developer.mozilla.org/en-US/docs/Web/JavaScript",
        "reason": "Learn modern JavaScript for web development."
    },

    "react": {
        "course": "https://react.dev/learn",
        "reason": "Learn React and build modern user interfaces."
    },

    "machine learning": {
        "course": "https://www.coursera.org/learn/machine-learning",
        "reason": "Build a strong foundation in Machine Learning."
    },

    "docker": {
        "course": "https://docs.docker.com/get-started/",
        "reason": "Learn containerization and Docker fundamentals."
    },

    "html": {
        "course": "https://developer.mozilla.org/en-US/docs/Learn/HTML",
        "reason": "Learn the fundamentals of HTML and web structure."
    },

    "css": {
        "course": "https://developer.mozilla.org/en-US/docs/Learn/CSS",
        "reason": "Learn modern CSS and responsive web design."
    },

    "git": {
        "course": "https://git-scm.com/book/en/v2",
        "reason": "Learn Git version control and collaboration workflows."
    },

    "django": {
        "course": "https://docs.djangoproject.com/en/stable/intro/tutorial01/",
        "reason": "Learn Django web development and backend architecture."
    },

    "data science": {
        "course": "https://www.coursera.org/specializations/jhu-data-science",
        "reason": "Develop data analysis and data science skills."
    }

}


def recommend_courses(missing_skills):

    courses = []

    for skill in missing_skills:

        skill_key = skill.lower().strip()

        if skill_key in COURSE_LINKS:

            course_data = COURSE_LINKS[skill_key].copy()

            course_data["skill"] = skill

            courses.append(course_data)

    return courses