# resume_analyzer.py

import fitz  # PyMuPDF
import re


def extract_text_from_pdf(pdf_file):
    """
    Extracts text from uploaded PDF file.
    """
    text = ""
    with fitz.open(stream=pdf_file.read(), filetype="pdf") as doc:
        for page in doc:
            text += page.get_text()
    return text


# 🔹 Rule-based Role Classification (No API)
def classify_resume(text):
    """
    Classifies resume into job roles using keyword matching.
    """
    text = text.lower()

    roles_keywords = {
        "Data Scientist": ["machine learning", "data science", "pandas", "numpy", "statistics", "model"],
        "Machine Learning Engineer": ["ml", "deep learning", "tensorflow", "pytorch", "model deployment"],
        "Software Engineer": ["java", "c++", "algorithms", "data structures", "oop"],
        "Web Developer": ["html", "css", "javascript", "react", "node", "frontend", "backend"],
        "DevOps Engineer": ["docker", "kubernetes", "ci/cd", "aws", "linux"],
        "Data Analyst": ["excel", "sql", "tableau", "power bi", "data visualization"]
    }

    scores = {}

    for role, keywords in roles_keywords.items():
        score = sum(1 for keyword in keywords if keyword in text)
        scores[role] = score

    # Get best match
    predicted_role = max(scores, key=scores.get)

    return {
        "role": predicted_role,
        "confidence": scores[predicted_role],
        "all_scores": scores
    }


# 🔹 Skill Extraction
def extract_skills(text):
    """
    Basic keyword-based skill extraction.
    """
    skills_db = [
        "Python", "Machine Learning", "Deep Learning",
        "NLP", "TensorFlow", "PyTorch",
        "Docker", "Kubernetes", "SQL", "AWS",
        "Flask", "Django", "React", "Power BI", "Tableau"
    ]

    found_skills = [
        skill for skill in skills_db
        if re.search(r"\b" + re.escape(skill.lower()) + r"\b", text.lower())
    ]

    return found_skills


# 🔹 Main Function
def analyze_resume(pdf_file):
    """
    Main function to integrate into AI Hub.
    """
    text = extract_text_from_pdf(pdf_file)

    result = {
        "predicted_role": classify_resume(text),
        "skills": extract_skills(text)
    }

    return result