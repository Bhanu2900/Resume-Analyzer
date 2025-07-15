def generate_improvement_tips(missing_skills):
    # Simple bullet point suggestions
    tips = []
    for skill in sorted(missing_skills):
        tips.append(f"✔ Add a line like: 'Experience with {skill} in relevant projects or internships.'")
    return tips
