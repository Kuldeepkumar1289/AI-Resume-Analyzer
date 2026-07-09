from django.contrib.auth.models import User
from django.shortcuts import redirect
import json
import re
import spacy
import os
from openai import OpenAI

from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.conf import settings

from rest_framework.decorators import api_view
from rest_framework.response import Response
from reportlab.pdfgen import canvas

# Custom Module Imports
from .models import UserProfile
from .resume_rewriter import rewrite_resume
from .ai_feedback import generate_feedback
from .course_recommender import recommend_courses
from .job_recommender import recommend_jobs
from .job_matcher import match_resume_with_job
from .resume_reader import extract_text_from_resume
from .skill_detector import detect_skills
from .career_predictor import predict_career
from .skill_gap import find_missing_skills
from .roadmap_generator import generate_roadmap
from .ats_score import calculate_ats_score
from .resume_tips import get_resume_tips

# Setup
import os
from openai import OpenAI

# 1. OpenAI Client setup
client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY")
)

# 2. SpaCy Model ko YAHAN (Global level par) load karein, kisi function ke andar nahi!
try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    # Agar model cached na ho toh safely handle karne ke liye
    nlp = spacy.blank("en") 


TECH_KEYWORDS = ["python", "java", "sql", "html", "css", "javascript", "django", "react", "machine learning", "data science"]

def analyze_with_gpt(resume_text, job_description):
    """Sends text to GPT and returns a structured JSON response."""
    if not job_description:
        return None

    prompt = f"""
    Analyze the resume and job description.
    Resume: {resume_text[:4000]} 
    Job Description: {job_description[:2000]}

    Give output STRICTLY in JSON format:
    {{
        "matching_skills": [],
        "missing_skills": [],
        "score": 0,
        "feedback": ""
    }}
    """
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini", # Changed from 4.1-mini (typo fix)
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3,
            response_format={ "type": "json_object" }
        )
        return json.loads(response.choices[0].message.content)
    except Exception as e:
        print(f"GPT Error: {e}")
        return None

def extract_skills_ai(text):
    doc = nlp(text.lower())
    skills = [chunk.text.strip() for chunk in doc.noun_chunks]
    return list(set(skills))

def filter_skills(ai_skills):
    return list(set([tech for tech in TECH_KEYWORDS if any(tech in skill for skill in ai_skills)]))

# ✅ HOME / UPLOAD VIEW
@login_required
def upload_resume(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        branch = request.POST.get("branch")
        cgpa = request.POST.get("cgpa")
        resume_file = request.FILES.get("resume")
        job_description = request.POST.get("job_description") or ""

        if not resume_file:
            return render(request, "upload.html", {"error": "No resume file uploaded."})

        # ✅ Save Profile
        profile = UserProfile.objects.create(
            user=request.user,
            name=name, email=email, branch=branch, cgpa=cgpa, resume=resume_file
        )

        # 🔍 STEP 1: Text Extraction
        raw_text = extract_text_from_resume(profile.resume.path)
        
        # 🔥 STEP 2: CLEAN TEXT
        clean_text = raw_text.lower()
        clean_text = re.sub(r'[^a-zA-Z0-9 ]', ' ', clean_text)
        words = clean_text.split()

        # 🔥 STEP 3: SKILL DETECTION (Hardcoded List)
        all_possible_skills = ["python", "django", "html", "css", "javascript", "sql", "mysql", "data science", "git"]
        detected_skills = [skill for skill in all_possible_skills if all(word in words for word in skill.split())]

        if "mysql" in words and "sql" not in detected_skills:
            detected_skills.append("sql")

        # 🤖 STEP 4: GPT Analysis
        gpt_data = analyze_with_gpt(raw_text, job_description)
        
        # Extract GPT info or use defaults
        gpt_matching = gpt_data.get("matching_skills", []) if gpt_data else []
        gpt_missing = gpt_data.get("missing_skills", []) if gpt_data else []
        gpt_score = gpt_data.get("score", 0) if gpt_data else 0
        gpt_feedback = gpt_data.get("feedback", "No specific feedback available.") if gpt_data else ""

        # 🚀 STEP 5: Additional Pipeline Features
        career = predict_career(detected_skills)
        missing_skills_list = [s for s in all_possible_skills if s not in detected_skills]
        
        context = {
            "name": name,
            "skills": detected_skills,
            "career": career,
            "roadmap": generate_roadmap(career),
            "ats_score": calculate_ats_score(detected_skills, missing_skills_list),
            "tips": get_resume_tips(missing_skills_list),
            "jobs": recommend_jobs(career),
            "courses": recommend_courses(missing_skills_list),
            "feedback": gpt_feedback,
            "rewritten": rewrite_resume(detected_skills, missing_skills_list),
            "matching_skills": gpt_matching,
            "missing_skills": gpt_missing,
            "match_score": gpt_score,
        }
        return render(request, "result.html", context)

    return render(request, "upload.html")

# ✅ HISTORY VIEW
@login_required
def history(request):
    profiles = UserProfile.objects.filter(user=request.user).order_by('-id')
    return render(request, "history.html", {"profiles": profiles})

# ✅ DOWNLOAD PDF REPORT
@login_required
def download_report(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="resume_report.pdf"'
    p = canvas.Canvas(response)
    p.drawString(100, 800, "AI Resume Analysis Report")
    p.drawString(100, 760, f"Name: {request.GET.get('name', '')}")
    p.drawString(100, 740, f"Career: {request.GET.get('career', '')}")
    p.showPage()
    p.save()
    return response

def signup(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        if User.objects.filter(username=username).exists():
            return render(request, "signup.html", {
                "error": "Username already exists"
            })

        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        return redirect("login")

    return render(request, "signup.html")