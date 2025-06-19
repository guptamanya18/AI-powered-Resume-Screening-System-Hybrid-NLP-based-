# AI-powered-Resume-Screening-System-Hybrid-NLP-based-

# 🧠 AI Resume Screening System

## Overview
An intelligent system that parses resumes and matches them with job roles using NLP and ML.

## Features
- Resume parsing (PDF/DOCX/TXT)
- NLP entity extraction
- Semantic job matching
- Scoring system
- Optional Streamlit UI

## NLP Techniques Used
- Named Entity Recognition (SpaCy)
- TF-IDF + Cosine Similarity
- Custom Skill Extraction
- (Optional) BERT embeddings

## How to Run
```bash
pip install -r requirements.txt
python main.py
streamlit run ui/streamlit_app.py
