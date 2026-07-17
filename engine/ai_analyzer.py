import json
import time

from google import genai
from django.conf import settings


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
    "recommended_learning_skills": [],
    "improvement_suggestions": [],
    "resume_rewrite": {{
        "professional_summary": "",
        "improved_bullet_points": []
    }}
}}

Rules:
- Analyze any career field.
- Do not assume the candidate is from IT.
- ATS score must be between 0 and 100.
- Do not invent skills not present in the resume.
- Return valid JSON only.
"""

    # Primary + fallback models
    MODELS = [
    "gemini-2.5-flash-lite",
    "gemini-2.0-flash-lite",
    "gemini-2.5-flash",
    "gemini-3.5-flash",
    ]

    for model in models:

        for attempt in range(2):

            try:

                print(
                    f"Trying model: {model} | Attempt: {attempt + 1}"
                )

                response = client.models.generate_content(
                    model=model,
                    contents=prompt
                )

                response_text = response.text.strip()

                if response_text.startswith("```json"):
                    response_text = response_text.replace(
                        "```json",
                        "",
                        1
                    )

                if response_text.endswith("```"):
                    response_text = response_text[:-3]

                response_text = response_text.strip()

                return json.loads(response_text)

            except Exception as e:

                print(
                    f"AI ERROR [{model}] "
                    f"Attempt {attempt + 1}: {e}"
                )

                time.sleep(2)

    print("ALL GEMINI MODELS FAILED")

    return None