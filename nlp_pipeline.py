import spacy

nlp = spacy.load("en_core_web_sm")

def extract_entities(text):
    doc = nlp(text)
    skills = []
    education = []
    experience = []

    for ent in doc.ents:
        if ent.label_ == "ORG":
            experience.append(ent.text)
        elif ent.label_ == "PERSON":
            continue
        elif ent.label_ in ["EDUCATION", "DEGREE", "GPE"]:
            education.append(ent.text)

    return {
        "skills": extract_skills(text),
        "education": list(set(education)),
        "experience": list(set(experience))
    }

def extract_skills(text):
    predefined_skills = ['Python', 'Java', 'Machine Learning', 'Data Science', 'SQL', 'Excel', 'NLP', 'Deep Learning']
    found = [skill for skill in predefined_skills if skill.lower() in text.lower()]
    return found
