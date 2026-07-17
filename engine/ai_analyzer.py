import json
from google import genai
from django.conf import settings


# Gemini Client
client = genai.Client(
    api_key=settings.GEMINI_API_KEY
)


def analyze_resume_with_ai(resume_text):

    prompt = f"""
You are an expert Resume Analyst, ATS Specialist,
Career Coach, and Recruitment Consultant.

Analyze this resume carefully:

RESUME:
{resume_text[:12000]}

Return ONLY valid JSON in exactly this structure:

{{
    "resume_summary": "",
    "candidate_profile": {{
        "current_role": "",
        "experience_level": "",
        "industry": "",
        "education": ""
    }},
    "skills": {{
        "technical": [],
        "soft": [],
        "tools": [],
        "domain": []
    }},
    "missing_skills": [],
    "recommended_careers": [
        {{
            "role": "",
            "reason": ""
        }}
    ],
    "ats_analysis": {{
        "score": 0,
        "strengths": [],
        "weaknesses": []
    }},
    "roadmap": [],
    "recommended_learning_skills": []

    ],
    "recommended_jobs": [],
    "improvement_suggestions": [],
    "resume_rewrite": {{
        "professional_summary": "",
        "improved_bullet_points": []
    }}
}}

Rules:

For recommended_courses:

- In recommended_learning_skills, return only skills that the candidate should learn.
- Do not generate URLs.
- Do not generate course names.
"""

    try:

        response = client.models.generate_content(
            model="gemini-3.5-flash",
            contents=prompt
        )

        response_text = response.text.strip()

        # Remove Markdown JSON wrapper if Gemini adds it
        if response_text.startswith("```json"):
            response_text = response_text[7:]

        if response_text.endswith("```"):
            response_text = response_text[:-3]

        response_text = response_text.strip()

        return json.loads(response_text)

    except Exception as e:

        print("AI ANALYSIS ERROR:", e)

        return None