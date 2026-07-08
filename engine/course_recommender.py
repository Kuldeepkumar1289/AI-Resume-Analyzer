def recommend_courses(missing_skills):

    course_map = {

        "Python": "https://www.coursera.org/learn/python",

        "Java": "https://www.udemy.com/course/java-programming",

        "React": "https://www.freecodecamp.org/learn/react",

        "Docker": "https://www.udemy.com/course/docker",

        "Machine Learning": "https://www.coursera.org/learn/machine-learning",

        "SQL": "https://www.w3schools.com/sql/"

    }

    courses = []

    for skill in missing_skills:
        if skill in course_map:
            courses.append({
                "skill": skill,
                "course": course_map[skill]
            })

    return courses