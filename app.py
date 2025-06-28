import streamlit as st
import spacy

st.title("Resume Analyzer")
st.write("Upload your resume to get started!")

uploaded_file = st.file_uploader("Choose a resume file", type=["pdf", "docx"])

if uploaded_file:
    st.success("Resume uploaded successfully!")
    st.write("File name:", uploaded_file.name)

    # Load spaCy model
    nlp = spacy.load("en_core_web_sm")
    doc = nlp("This is a test sentence for SpaCy.")
    st.write("SpaCy tokens:", [token.text for token in doc])


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


from matcher import match_resume_to_jobs

st.subheader("Matching Job Roles:")
matches = match_resume_to_jobs(result["skills"], job_listings)

for match in matches:
    st.write(f"🔹 **{match['title']}** at {match['company']} — Match: {match['similarity']}%")

