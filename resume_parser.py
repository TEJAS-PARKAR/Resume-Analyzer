import re
import spacy
from io import BytesIO
from pdfminer.high_level import extract_text
from docx import Document

# Load SpaCy model
nlp = spacy.load("en_core_web_sm")

# Extract text from PDF
def extract_text_from_pdf(file):
    text = extract_text(file)
    return text

# Extract text from DOCX
def extract_text_from_docx(file):
    doc = Document(file)
    return "\n".join([para.text for para in doc.paragraphs])

# Extract email
def extract_email(text):
    match = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)
    return match[0] if match else None

# Extract phone
def extract_phone(text):
    match = re.findall(r"\+?\d[\d\s\-\(\)]{8,15}", text)
    return match[0] if match else None

# Extract skills (using a sample keyword list)
def extract_skills(text):
    skill_keywords = ["Python", "C++", "Java", "HTML", "CSS", "SQL", "Machine Learning", "Data Analysis"]
    found = []
    for skill in skill_keywords:
        if re.search(r"\b" + re.escape(skill) + r"\b", text, re.IGNORECASE):
            found.append(skill)
    return found

# Master function
def parse_resume(file, filename):
    if filename.endswith(".pdf"):
        text = extract_text_from_pdf(file)
    elif filename.endswith(".docx"):
        text = extract_text_from_docx(file)
    else:
        return {"error": "Unsupported file format."}

    doc = nlp(text)
    name = [ent.text for ent in doc.ents if ent.label_ == "PERSON"]
    email = extract_email(text)
    phone = extract_phone(text)
    skills = extract_skills(text)

    return {
        "name": name[0] if name else None,
        "email": email,
        "phone": phone,
        "skills": skills
    }
