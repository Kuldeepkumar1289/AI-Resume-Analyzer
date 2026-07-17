from django.contrib.auth.models import User
from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from reportlab.pdfgen import canvas

from .models import UserProfile
from .resume_reader import extract_text_from_resume
from .ai_analyzer import analyze_resume_with_ai
from .course_recommender import recommend_courses
from .job_recommender import recommend_jobs


# HELPER FUNCTION

def ensure_list(data):
    """
    Ensures that AI response values are always lists.
    """

    if not data:
        return []

    if isinstance(data, list):
        return data

    if isinstance(data, str):
        return [data]

    return []


# UPLOAD AND ANALYZE RESUME

@login_required
def upload_resume(request):

    if request.method == "POST":

        # 1. GET FORM DATA

        name = request.POST.get(
            "name",
            ""
        ).strip()

        email = request.POST.get(
            "email",
            ""
        ).strip()

        branch = request.POST.get(
            "branch",
            ""
        ).strip()

        cgpa = request.POST.get(
            "cgpa"
        ) or None

        resume_file = request.FILES.get(
            "resume"
        )

        # 2. CHECK RESUME

        if not resume_file:

            return render(

                request,

                "upload.html",

                {
                    "error":
                    "Please upload your resume."
                }

            )

        # 3. SAVE RESUME

        profile = UserProfile.objects.create(

            user=request.user,

            name=name,

            email=email,

            branch=branch,

            cgpa=cgpa,

            resume=resume_file

        )

        # 4. EXTRACT RESUME TEXT

        raw_text = extract_text_from_resume(

            profile.resume.path

        )


        if not raw_text:

            return render(

                request,

                "upload.html",

                {

                    "error":
                    "Could not extract text from the resume."

                }

            )

        # 5. AI ANALYSIS

        ai_data = analyze_resume_with_ai(

            raw_text

        )


        if not ai_data:

            return render(

                request,

                "upload.html",

                {

                    "error":
                    "AI analysis failed. Please try again."

                }

            )

        # 6. RESUME SUMMARY

        resume_summary = ai_data.get(

            "resume_summary",

            "Resume analysis completed successfully."

        )

        # 7. CANDIDATE PROFILE

        candidate_profile = ai_data.get(

            "candidate_profile",

            {}

        )

        # 8. SKILLS

        skills_data = ai_data.get(

            "skills",

            {}

        )


        technical_skills = ensure_list(

            skills_data.get(

                "technical",

                []

            )

        )


        soft_skills = ensure_list(

            skills_data.get(

                "soft",

                []

            )

        )


        tools = ensure_list(

            skills_data.get(

                "tools",

                []

            )

        )


        domain_skills = ensure_list(

            skills_data.get(

                "domain",

                []

            )

        )


        # Combine all skills

        detected_skills = (

            technical_skills

            + soft_skills

            + tools

            + domain_skills

        )


        # Remove duplicate skills

        detected_skills = list(

            dict.fromkeys(

                detected_skills

            )

        )

        # 9. MISSING SKILLS

        missing_skills = ensure_list(

            ai_data.get(

                "missing_skills",

                []

            )

        )

        # 10. CAREER RECOMMENDATIONS

        recommended_careers = ensure_list(

            ai_data.get(

                "recommended_careers",

                []

            )

        )


        # 11. PRIMARY CAREER

        primary_career = (

            "Career Recommendation"

        )


        if recommended_careers:

            first_career = (

                recommended_careers[0]

            )


            if isinstance(

                first_career,

                dict

            ):

                primary_career = (

                    first_career.get(

                        "role",

                        "Career Recommendation"

                    )

                )


            else:

                primary_career = str(

                    first_career

                )


        # 12. ATS ANALYSIS

        ats_analysis = ai_data.get(

            "ats_analysis",

            {}

        )


        ats_score = ats_analysis.get(

            "score",

            0

        )


        # Make sure score is valid

        try:

            ats_score = int(

                ats_score

            )

        except (

            ValueError,

            TypeError

        ):

            ats_score = 0


        # Keep score between 0 and 100

        ats_score = max(

            0,

            min(

                ats_score,

                100

            )

        )


        ats_strengths = ensure_list(

            ats_analysis.get(

                "strengths",

                []

            )

        )


        ats_weaknesses = ensure_list(

            ats_analysis.get(

                "weaknesses",

                []

            )

        )


        # 13. ROADMAP

        roadmap = ensure_list(

            ai_data.get(

                "roadmap",

                []

            )

        )


        # 14. RECOMMENDED COURSES

        recommended_learning_skills = (

            ensure_list(

                ai_data.get(

                    "recommended_learning_skills",

                    []

                )

            )

        )


        if not recommended_learning_skills:

            recommended_learning_skills = (

                missing_skills

            )


        courses = recommend_courses(

            recommended_learning_skills

        )


        # 15. RECOMMENDED JOBS

        jobs = recommend_jobs(

            primary_career

        )


        # 16. IMPROVEMENT SUGGESTIONS

        improvement_suggestions = (

            ensure_list(

                ai_data.get(

                    "improvement_suggestions",

                    []

                )

            )

        )


        # 17. SAVE AI ANALYSIS IN DATABASE

        profile.resume_summary = (

            resume_summary

        )


        profile.detected_skills = (

            detected_skills

        )


        profile.missing_skills = (

            missing_skills

        )


        profile.recommended_careers = (

            recommended_careers

        )


        profile.roadmap = (

            roadmap

        )


        profile.recommended_courses = (

            courses

        )


        profile.recommended_jobs = (

            jobs

        )


        profile.improvement_suggestions = (

            improvement_suggestions

        )


        profile.ats_score = (

            ats_score

        )


        profile.save()


        # 18. RESULT PAGE CONTEXT

        context = {

            "name": name,

            "email": email,

            "summary": resume_summary,

            "skills": detected_skills,

            "career": primary_career,

            "recommended_careers": (

                recommended_careers

            ),

            "missing_skills": (

                missing_skills

            ),

            "ats_score": ats_score,

            "ats_strengths": (

                ats_strengths

            ),

            "ats_weaknesses": (

                ats_weaknesses

            ),

            "roadmap": roadmap,

            "courses": courses,

            "jobs": jobs,

            "tips": (

                improvement_suggestions

            ),

            "feedback": (

                improvement_suggestions

            ),

            "matched_skills": (

                detected_skills

            ),

            "missing_job_skills": (

                missing_skills

            ),

            "match_score": ats_score,

            "candidate_profile": (

                candidate_profile

            ),

        }


        # 19. SHOW RESULT PAGE

        return render(

            request,

            "result.html",

            context

        )


    # GET REQUEST

    return render(

        request,

        "upload.html"

    )


# HISTORY

@login_required
def history(request):

    profiles = (

        UserProfile.objects.filter(

            user=request.user

        )

        .order_by(

            "-created_at"

        )

    )


    return render(

        request,

        "history.html",

        {

            "profiles": profiles

        }

    )


# VIEW OLD ANALYSIS

@login_required
def view_analysis(

    request,

    profile_id

):

    profile = get_object_or_404(

        UserProfile,

        id=profile_id,

        user=request.user

    )


    recommended_careers = (

        profile.recommended_careers

    )


    primary_career = (

        "Career Recommendation"

    )


    if recommended_careers:

        first_career = (

            recommended_careers[0]

        )


        if isinstance(

            first_career,

            dict

        ):

            primary_career = (

                first_career.get(

                    "role",

                    "Career Recommendation"

                )

            )


        else:

            primary_career = str(

                first_career

            )


    # for Old database records 
    # if jobs/courses is empty 

    courses = (

        profile.recommended_courses

    )


    if not courses:

        courses = recommend_courses(

            profile.missing_skills

        )


    jobs = (

        profile.recommended_jobs

    )


    if not jobs:

        jobs = recommend_jobs(

            primary_career

        )


    context = {

        "name": profile.name,

        "email": profile.email,

        "summary": profile.resume_summary,

        "skills": profile.detected_skills,

        "career": primary_career,

        "recommended_careers": (

            profile.recommended_careers

        ),

        "missing_skills": (

            profile.missing_skills

        ),

        "ats_score": profile.ats_score,

        "roadmap": profile.roadmap,

        "courses": courses,

        "jobs": jobs,

        "tips": (

            profile.improvement_suggestions

        ),

        "feedback": (

            profile.improvement_suggestions

        ),

        "matched_skills": (

            profile.detected_skills

        ),

        "missing_job_skills": (

            profile.missing_skills

        ),

        "match_score": (

            profile.ats_score

        ),

    }


    return render(

        request,

        "result.html",

        context

    )


# DOWNLOAD PDF REPORT

@login_required
def download_report(request):

    response = HttpResponse(

        content_type="application/pdf"

    )


    response[

        "Content-Disposition"

    ] = (

        'attachment; '

        'filename="resume_report.pdf"'

    )


    pdf = canvas.Canvas(

        response

    )


    pdf.drawString(

        100,

        800,

        "AI Resume Analysis Report"

    )


    pdf.drawString(

        100,

        760,

        f"Name: "

        f"{request.GET.get('name', '')}"

    )


    pdf.drawString(

        100,

        740,

        f"Career: "

        f"{request.GET.get('career', '')}"

    )


    pdf.drawString(

        100,

        720,

        f"ATS Score: "

        f"{request.GET.get('ats_score', '')}"

    )


    pdf.showPage()


    pdf.save()


    return response


# SIGNUP

def signup(request):

    if request.method == "POST":

        username = request.POST.get(

            "username",

            ""

        ).strip()


        email = request.POST.get(

            "email",

            ""

        ).strip()


        password = request.POST.get(

            "password",

            ""

        )


        if User.objects.filter(

            username=username

        ).exists():

            return render(

                request,

                "signup.html",

                {

                    "error":

                    "Username already exists."

                }

            )


        User.objects.create_user(

            username=username,

            email=email,

            password=password

        )


        return redirect(

            "login"

        )


    return render(

        request,

        "signup.html"

    )