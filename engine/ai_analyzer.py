import json
import time

from google import genai
from google.genai import types
from django.conf import settings


# GEMINI CLIENT

client = genai.Client(
    api_key=settings.GEMINI_API_KEY
)

# AI RESUME ANALYZER

def analyze_resume_with_ai(resume_text):

    prompt = f"""
You are an expert Resume Analyst, ATS Specialist,
Career Coach, and Recruitment Consultant.

Analyze this resume carefully.

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

RULES:

- Analyze any career field.
- Do not assume the candidate is from IT.
- ATS score must be between 0 and 100.
- Analyze the actual resume carefully.
- Do not invent skills that are not present in the resume.
- Recommend missing skills that are genuinely useful for the candidate's target career.
- Recommended learning skills must be skill names only.
- Do not provide course URLs.
- Return valid JSON only.
"""


    # PRIMARY + FALLBACK GEMINI MODELS

    MODELS = [

        "gemini-2.5-flash-lite",

        "gemini-2.0-flash-lite",

        "gemini-2.5-flash",

        "gemini-3.5-flash",

    ]

    # TRY EACH MODEL

    for model in MODELS:

        for attempt in range(2):

            try:

                print(
                    f"Trying model: {model} | "
                    f"Attempt: {attempt + 1}"
                )


                response = client.models.generate_content(

                    model=model,

                    contents=prompt,

                    config=types.GenerateContentConfig(

                        response_mime_type="application/json"

                    )

                )

                # GET RESPONSE TEXT

                response_text = response.text.strip()

                # REMOVE MARKDOWN JSON BLOCK

                if response_text.startswith("```json"):

                    response_text = response_text.replace(

                        "```json",

                        "",

                        1

                    )


                if response_text.startswith("```"):

                    response_text = response_text.replace(

                        "```",

                        "",

                        1

                    )


                if response_text.endswith("```"):

                    response_text = response_text[:-3]


                response_text = response_text.strip()

                # CONVERT JSON STRING TO PYTHON DICT

                ai_data = json.loads(response_text)


                print(
                    f"AI ANALYSIS SUCCESSFUL "
                    f"USING MODEL: {model}"
                )


                return ai_data


            except Exception as e:


                print(

                    f"AI ERROR [{model}] "

                    f"Attempt {attempt + 1}: {e}"

                )


                # Wait before retry

                time.sleep(2)

    # ALL MODELS FAILED

    print(
        "ALL GEMINI MODELS FAILED"
    )


    return None