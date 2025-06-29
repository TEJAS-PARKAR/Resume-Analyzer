import streamlit as st
import spacy
from resume_parser import parse_resume
from matcher import match_resume_to_jobs

# Load spaCy model only once
nlp = spacy.load("en_core_web_sm")

st.title("Resume Analyzer")
st.write("Upload your resume to get started!")

uploaded_file = st.file_uploader("Choose a resume file", type=["pdf", "docx"])

if uploaded_file:
    st.success("Resume uploaded successfully!")
    st.write("File name:", uploaded_file.name)

    with st.spinner("Parsing resume..."):
        result = parse_resume(uploaded_file, uploaded_file.name)

    st.subheader("Extracted Info:")
    st.write("**Name:**", result["name"])
    st.write("**Email:**", result["email"])
    st.write("**Phone:**", result["phone"])
    st.write("**Skills:**", ", ".join(result["skills"]))

    # Sample job listings
    job_listings = [
        {
            "title": "Python Developer Intern",
            "company": "TechNova",
            "description": "We need a developer with Python, SQL, and basic ML knowledge."
        },
        {
            "title": "Frontend Web Developer",
            "company": "CodeCraft",
            "description": "Looking for skills in HTML, CSS, JavaScript, React."
        },
        {
            "title": "Data Analyst Intern",
            "company": "InsightAI",
            "description": "Data analysis, Excel, Python, Pandas, and visualization."
        }
    ]

    st.subheader("Matching Job Roles:")
    matches = match_resume_to_jobs(result["skills"], job_listings)

    for match in matches:
        st.write(f"🔹 **{match['title']}** at {match['company']} — Match: {match['similarity']}%")
