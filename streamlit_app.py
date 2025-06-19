import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from app.parser import extract_text_from_pdf as extract_text
from app.nlp_pipeline import extract_entities
from app.matching import calculate_similarity


st.title("🧠 Resume Screening System")

uploaded_resume = st.file_uploader("Upload Resume", type=['pdf', 'docx'])
job_description = st.text_area("Paste Job Description")

if uploaded_resume and job_description:
    with open("temp_resume", "wb") as f:
        f.write(uploaded_resume.read())

    text = extract_text("temp_resume")
    entities = extract_entities(text)
    score = calculate_similarity(text, job_description)

    st.subheader(f"Compatibility Score: {score*100:.2f}%")
    st.write("**Extracted Skills:**", entities['skills'])
    st.write("**Experience:**", entities['experience'])
    st.write("**Education:**", entities['education'])
