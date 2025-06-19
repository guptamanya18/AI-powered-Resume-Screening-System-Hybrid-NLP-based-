from app.parser import extract_text_from_pdf as extract_text

from app.nlp_pipeline import extract_entities
from app.matching import calculate_similarity

resume_path = "resumes/sample_resume.pdf"
job_desc_path = "job_descriptions/data_analyst.txt"

resume_text = extract_text(r"C:\Users\hp\Resume Building System\Resumes\resume.pdf")
job_text = open(r"C:\Users\hp\Resume Building System\data_analyst.txt").read()

entities = extract_entities(resume_text)
score = calculate_similarity(resume_text, job_text)

print(f"Match Score: {score*100:.2f}%")
print("Extracted Info:", entities)
