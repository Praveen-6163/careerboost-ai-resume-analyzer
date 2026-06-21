import os
import json
import PyPDF2
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def extract_text_from_pdf(pdf_file):
    """
    Extracts text from a PDF file object or file path.
    """
    text = ""
    try:
        reader = PyPDF2.PdfReader(pdf_file)
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    except Exception as e:
        raise ValueError(f"Failed to read PDF file: {str(e)}")
    
    if not text.strip():
        raise ValueError("The uploaded PDF seems to be empty or image-only (OCR is not supported).")
    
    return text.strip()

def get_gemini_client():
    """
    Configures and returns the Gemini model client.
    """
    key = os.getenv("GEMINI_API_KEY")
    if not key:
        raise ValueError("GEMINI_API_KEY environment variable is not configured.")
    
    genai.configure(api_key=key)
    model_name = "gemini-2.5-flash"
    generation_config = {
        "response_mime_type": "application/json",
        "temperature": 0.2
    }
    return genai.GenerativeModel(model_name, generation_config=generation_config)

def clean_and_parse_json(response_text):
    """
    Safely parses JSON responses from the Gemini API, stripping out any markdown formatting if present.
    """
    text = response_text.strip()
    if text.startswith("```"):
        if text.startswith("```json"):
            text = text[7:]
        else:
            text = text[3:]
        if text.endswith("```"):
            text = text[:-3]
        text = text.strip()
    
    try:
        return json.loads(text)
    except json.JSONDecodeError as e:
        raise ValueError(f"Failed to parse model response as JSON: {str(e)}")

def heuristic_analyze_resume(resume_text):
    """
    Analyzes the resume text locally using heuristics (fallback when API is unavailable).
    """
    text_lower = resume_text.lower()
    
    # Skills dictionary matching
    tech_keywords = {
        "python": "Python", "java": "Java", "javascript": "JavaScript", "c++": "C++", "c#": "C#",
        "sql": "SQL", "postgresql": "PostgreSQL", "mysql": "MySQL", "mongodb": "MongoDB",
        "redis": "Redis", "docker": "Docker", "kubernetes": "Kubernetes", "aws": "AWS",
        "azure": "Azure", "git": "Git", "ci/cd": "CI/CD", "streamlit": "Streamlit",
        "django": "Django", "fastapi": "FastAPI", "react": "React", "html": "HTML", "css": "CSS"
    }
    
    soft_keywords = {
        "leadership": "Leadership", "communication": "Communication", "teamwork": "Teamwork",
        "agile": "Agile", "scrum": "Scrum", "problem solving": "Problem Solving",
        "mentoring": "Mentoring", "collaboration": "Collaboration", "negotiation": "Negotiation"
    }
    
    tech_found = [val for key, val in tech_keywords.items() if key in text_lower]
    soft_found = [val for key, val in soft_keywords.items() if key in text_lower]
    
    # Missing skills determination
    all_common_tech = ["Docker", "Kubernetes", "Redis", "AWS", "CI/CD", "FastAPI"]
    missing_tech = [s for s in all_common_tech if s.lower() not in text_lower]
    
    # Calculate scores based on findings
    score = 65 + min(len(tech_found) * 3, 20) + min(len(soft_found) * 2, 10)
    score = min(score, 98)
    
    # Recommended roles
    roles = []
    if "python" in text_lower or "fastapi" in text_lower or "django" in text_lower:
        roles.append("Python Backend Developer")
    if "aws" in text_lower or "docker" in text_lower or "kubernetes" in text_lower:
        roles.append("DevOps & Cloud Engineer")
    if "sql" in text_lower or "postgres" in text_lower:
        roles.append("Database Specialist")
    if not roles:
        roles = ["Software Engineer", "Full Stack Developer"]
        
    # Actionable suggestions
    suggestions = []
    if len(tech_found) < 5:
        suggestions.append({"priority": "High", "area": "Technical Skills", "suggestion": "Add more software languages and libraries to broaden technical indexing."})
    if "docker" not in text_lower:
        suggestions.append({"priority": "Medium", "area": "DevOps Practices", "suggestion": "Incorporate containerization keywords like Docker or Kubernetes to align with senior roles."})
    if "git" not in text_lower:
        suggestions.append({"priority": "High", "area": "Version Control", "suggestion": "Explicitly mention Git workflow practices to show collaborative development experience."})
    if len(resume_text) > 1500:
        suggestions.append({"priority": "Low", "area": "Formatting", "suggestion": "Ensure the resume content fits onto 1-2 pages maximum for readability."})
    else:
        suggestions.append({"priority": "Medium", "area": "Quantifying Impact", "suggestion": "Add metrics, percentages, or transaction volumes to highlight your project achievements."})
        
    # Tailored interview questions
    questions = [
        {
            "question": f"How have you successfully implemented {tech_found[0]} in your past projects?" if tech_found else "Can you walk me through your technical stack?",
            "intent": "Verify operational capability in listed technologies.",
            "suggested_answer": "Structure your response using the STAR method: describe a problem, the actions you took, and the final positive impact."
        },
        {
            "question": "Describe a time you handled a technical bottleneck or slow query. How did you diagnose it?",
            "intent": "Assess troubleshooting methods and analytical mindset.",
            "suggested_answer": "Detail debugging tools, profiling logs, indexing databases, or caching layers you set up to optimize speed."
        }
    ]
    
    return {
        "ats_score": int(score),
        "resume_strength": int(score + 3),
        "profile_summary": "Extracted profile details indicate a balanced combination of development capabilities. Clear structure with potential to optimize keyword weights.",
        "technical_skills": tech_found if tech_found else ["Software Engineering"],
        "soft_skills": soft_found if soft_found else ["Collaboration"],
        "missing_skills": missing_tech,
        "recommended_roles": roles[:3],
        "improvement_suggestions": suggestions,
        "interview_questions": questions
    }

def heuristic_analyze_match(resume_text, job_desc):
    """
    Compares resume and job description locally using keyword overlap (fallback).
    """
    res_lower = resume_text.lower()
    jd_lower = job_desc.lower()
    
    keywords = ["python", "java", "sql", "aws", "docker", "kubernetes", "git", "ci/cd", "streamlit", "django", "fastapi", "react", "scrum", "agile", "leadership", "communication"]
    
    jd_words = [w for w in keywords if w in jd_lower]
    matching = [w.title() for w in jd_words if w in res_lower]
    missing = [w.title() for w in jd_words if w not in res_lower]
    
    if jd_words:
        pct = int((len(matching) / len(jd_words)) * 100)
    else:
        pct = 60
        
    pct = max(min(pct, 98), 20)
    
    return {
        "match_score": pct,
        "resume_strength": int((pct + 85) / 2),
        "profile_summary": f"Matching assessment indicates a {pct}% keyword alignment. Strengths found in core overlaps, with critical missing keywords identified.",
        "matching_skills": matching if matching else ["General Skills"],
        "missing_skills": missing if missing else ["No Critical Gaps"],
        "job_description_alignment": f"High keyword overlap in {', '.join(matching[:3]) if matching else 'general areas'}. Missing key skills such as {', '.join(missing[:3]) if missing else 'none'}.",
        "improvement_suggestions": [
            {"priority": "High", "area": "Keyword Optimization", "suggestion": f"Incorporate the missing keywords: {', '.join(missing[:3])} to bypass ATS filtering layers."}
        ] if missing else [{"priority": "Low", "area": "Formatting", "suggestion": "Ensure the contact details and profile summary are on page 1."}],
        "interview_questions": [
            {
                "question": f"The job description highlights the need for {missing[0]} skills. Can you describe any familiarity or relevant learning path?" if missing else "How does your past experience align with this position?",
                "intent": "Evaluate readiness for target tech stacks.",
                "suggested_answer": "Acknowledge missing gaps openly, highlight related conceptual knowledge, and describe your fast-learning workflow."
            }
        ]
    }

def analyze_resume_general(resume_text):
    """
    Analyzes the resume in isolation. Fallback to heuristic parser if API is unavailable.
    """
    try:
        model = get_gemini_client()
        prompt = f"""
        You are an expert HR Manager and Senior Recruiter. Analyze the following resume text and provide a professional feedback evaluation in JSON format.
        
        Resume Text:
        {resume_text}
        
        Provide your evaluation in the following JSON schema:
        {{
          "ats_score": <integer between 0 and 100 representing general ATS compatibility and structure>,
          "resume_strength": <integer between 0 and 100 representing profile completeness, depth of projects, and phrasing quality>,
          "profile_summary": "<a concise 2-3 sentence overview of the candidate's professional profile>",
          "technical_skills": [<array of extracted technical/hard skills, e.g. languages, frameworks, tools>],
          "soft_skills": [<array of extracted soft skills, e.g. leadership, communication, team-work>],
          "missing_skills": [<array of skills/technologies that are highly demanded for their profile/industry but not listed in the resume>],
          "recommended_roles": [<array of 3-5 suitable job roles for this candidate>],
          "improvement_suggestions": [
            {{
              "priority": "<High, Medium, or Low>",
              "area": "<aspect of resume needing work, e.g., 'Quantifiable Impact', 'Skills Organization', 'Formatting'>",
              "suggestion": "<actionable, specific advice on how to improve this area>"
            }}
          ],
          "interview_questions": [
            {{
              "question": "<sample interview question tailored to their profile/projects>",
              "intent": "<the recruiting intent behind asking this question>",
              "suggested_answer": "<advice on how the candidate can answer effectively>"
            }}
          ]
        }}
        
        Strictly adhere to the JSON schema. Do not output anything other than valid JSON.
        """
        response = model.generate_content(prompt)
        return clean_and_parse_json(response.text)
    except Exception as e:
        return heuristic_analyze_resume(resume_text)

def analyze_resume_match(resume_text, job_description):
    """
    Compares the resume text with a specific job description to compute ATS match score, matching/missing skills, and tailored suggestions.
    """
    try:
        model = get_gemini_client()
        prompt = f"""
        You are an expert ATS (Applicant Tracking System) matching scanner. Compare the following resume text with the target job description. Provide a detailed matching analysis in JSON format.
        
        Resume Text:
        {resume_text}
        
        Job Description:
        {job_description}
        
        Provide your evaluation in the following JSON schema:
        {{
          "match_score": <integer between 0 and 100 representing how well the resume matches the job description requirements>,
          "resume_strength": <integer between 0 and 100 representing profile completeness and project depth relative to this job description>,
          "profile_summary": "<a concise 2-3 sentence overview of how well the candidate fits this specific job description>",
          "matching_skills": [<array of skills from the job description that ARE present in the resume>],
          "missing_skills": [<array of key skills, keywords, or certifications from the job description that ARE NOT present or clearly highlighted in the resume>],
          "job_description_alignment": "<detailed description of alignment strengths and weaknesses relative to the role>",
          "improvement_suggestions": [
            {{
              "priority": "<High, Medium, or Low>",
              "area": "<aspect to fix for this specific role, e.g., 'Keyword Optimization', 'Experience Tailoring'>",
              "suggestion": "<highly specific advice to make the resume stand out for this job description>"
            }}
          ],
          "interview_questions": [
            {{
              "question": "<sample interview question combining their experience with this specific job description requirements>",
              "intent": "<why this matters for this role>",
              "suggested_answer": "<how to answer focusing on the match>"
            }}
          ]
        }}
        
        Strictly adhere to the JSON schema. Do not output anything other than valid JSON.
        """
        response = model.generate_content(prompt)
        return clean_and_parse_json(response.text)
    except Exception as e:
        return heuristic_analyze_match(resume_text, job_description)

def generate_html_report(analysis, match=None):
    """
    Generates a beautifully styled, printable HTML report for the user to download or print to PDF.
    """
    is_match_active = match is not None
    ats = analysis.get("ats_score", 0)
    strength = analysis.get("resume_strength", 0)
    match_score_str = f"{match.get('match_score', 0)}%" if is_match_active else "N/A"
    
    tech_badges = "".join([f'<span class="tag tag-tech">{s}</span>' for s in analysis.get("technical_skills", [])])
    soft_badges = "".join([f'<span class="tag tag-soft">{s}</span>' for s in analysis.get("soft_skills", [])])
    missing_badges = ""
    
    if is_match_active:
        missing_badges = "".join([f'<span class="tag tag-missing">{s}</span>' for s in match.get("missing_skills", [])])
    else:
        missing_badges = "".join([f'<span class="tag tag-missing">{s}</span>' for s in analysis.get("missing_skills", [])])

    suggestions = match.get("improvement_suggestions", []) if is_match_active else analysis.get("improvement_suggestions", [])
    roadmap_html = ""
    for item in suggestions:
        prio = item.get("priority", "Low")
        prio_color = "#ef4444" if prio.lower() == "high" else "#f59e0b" if prio.lower() == "medium" else "#3b82f6"
        roadmap_html += f"""
        <div class="roadmap-card" style="border-left: 5px solid {prio_color};">
            <div style="display:flex; justify-content:space-between; font-weight:bold; margin-bottom:5px;">
                <span>🛠️ {item.get('area', 'General')}</span>
                <span style="color:{prio_color}; font-size:0.8rem; text-transform:uppercase;">{prio} Priority</span>
            </div>
            <div style="color:#4b5563; font-size:0.9rem;">{item.get('suggestion', '')}</div>
        </div>
        """
        
    questions = match.get("interview_questions", []) if is_match_active else analysis.get("interview_questions", [])
    prep_html = ""
    for idx, q in enumerate(questions):
        prep_html += f"""
        <div style="margin-bottom: 15px; padding-bottom: 15px; border-bottom: 1px solid #e5e7eb;">
            <div style="font-weight: bold; color: #1e3a8a; margin-bottom: 5px;">Q{idx+1}: {q.get('question', '')}</div>
            <div style="font-size: 0.85rem; color: #6b7280; font-style: italic; margin-bottom: 5px;">Recruiter Intent: {q.get('intent', '')}</div>
            <div style="font-size: 0.9rem; color: #374151;"><strong>Suggested Response:</strong> {q.get('suggested_answer', '')}</div>
        </div>
        """

    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <title>CareerBoost AI Audit Report</title>
        <style>
            body {{ font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; color: #1f2937; margin: 40px; line-height: 1.5; }}
            .header {{ border-bottom: 2px solid #3b82f6; padding-bottom: 20px; margin-bottom: 30px; }}
            .title {{ font-size: 2.2rem; font-weight: 800; color: #1e3a8a; margin: 0; }}
            .subtitle {{ color: #6b7280; margin: 5px 0 0 0; }}
            .grid {{ display: grid; grid-template-columns: repeat(4, 1fr); gap: 20px; margin-bottom: 30px; }}
            .kpi-card {{ border: 1px solid #e5e7eb; border-radius: 8px; padding: 15px; text-align: center; background-color: #f9fafb; }}
            .kpi-title {{ font-size: 0.75rem; text-transform: uppercase; color: #6b7280; font-weight: bold; letter-spacing: 0.05em; }}
            .kpi-value {{ font-size: 2rem; font-weight: 800; margin: 10px 0; color: #1f2937; }}
            .panel {{ border: 1px solid #e5e7eb; border-radius: 8px; padding: 20px; margin-bottom: 25px; }}
            .panel-title {{ font-size: 1.2rem; font-weight: bold; color: #1e3a8a; border-bottom: 1px solid #e5e7eb; padding-bottom: 8px; margin-bottom: 15px; }}
            .tag {{ display: inline-block; padding: 4px 8px; border-radius: 20px; font-size: 0.8rem; margin: 3px; font-weight: bold; }}
            .tag-tech {{ background-color: #dbeafe; color: #1e40af; }}
            .tag-soft {{ background-color: #d1fae5; color: #065f46; }}
            .tag-missing {{ background-color: #fee2e2; color: #991b1b; }}
            .roadmap-card {{ border: 1px solid #e5e7eb; border-radius: 6px; padding: 12px; margin-bottom: 10px; background-color: #f9fafb; }}
        </style>
    </head>
    <body>
        <div class="header">
            <h1 class="title">CareerBoost AI Audit Report</h1>
            <p class="subtitle">SaaS Resume Health Evaluation & Target Role Match Analysis</p>
        </div>
        
        <div class="grid">
            <div class="kpi-card">
                <div class="kpi-title">ATS Score</div>
                <div class="kpi-value" style="color: #3b82f6;">{ats}%</div>
            </div>
            <div class="kpi-card">
                <div class="kpi-title">Job Match</div>
                <div class="kpi-value" style="color: #10b981;">{match_score_str}</div>
            </div>
            <div class="kpi-card">
                <div class="kpi-title">Resume Strength</div>
                <div class="kpi-value" style="color: #8b5cf6;">{strength}%</div>
            </div>
            <div class="kpi-card">
                <div class="kpi-title">Skill Gaps</div>
                <div class="kpi-value" style="color: #f43f5e;">{len(analysis.get('missing_skills', []))}</div>
            </div>
        </div>

        <div class="panel">
            <div class="panel-title">📋 Executive Summary</div>
            <div>{analysis.get('profile_summary', '')}</div>
            {f'<div style="margin-top:15px; padding-top:15px; border-top:1px dashed #e5e7eb;"><strong>Match Evaluation:</strong> {match.get("profile_summary", "")}</div>' if is_match_active else ''}
        </div>

        <div class="panel">
            <div class="panel-title">💻 Skills Analysis</div>
            <div style="margin-bottom:15px;"><strong>Technical Skills:</strong><br>{tech_badges}</div>
            <div style="margin-bottom:15px;"><strong>Soft Skills:</strong><br>{soft_badges}</div>
            <div><strong>Identified Skill Gaps:</strong><br>{missing_badges}</div>
        </div>

        <div class="panel">
            <div class="panel-title">💡 Actionable Optimization Roadmap</div>
            {roadmap_html}
        </div>

        <div class="panel">
            <div class="panel-title">💬 Tailored Interview Preparation</div>
            {prep_html}
        </div>
    </body>
    </html>
    """
    return html
