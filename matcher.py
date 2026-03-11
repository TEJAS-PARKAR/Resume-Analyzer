from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Function to match resume text with job descriptions
def match_resume_to_jobs(resume_skills, job_listings):
    results = []

    resume_text = " ".join(resume_skills)

    for job in job_listings:
        job_text = job["description"]
        vectorizer = TfidfVectorizer()
        vectors = vectorizer.fit_transform([resume_text, job_text])
        similarity = cosine_similarity(vectors[0], vectors[1])[0][0]
        results.append({
            "title": job["title"],
            "company": job.get("company", "Unknown"),
            "similarity": round(similarity * 100, 2)
        })

    # Sort by highest match
    results.sort(key=lambda x: x["similarity"], reverse=True)
    return results
