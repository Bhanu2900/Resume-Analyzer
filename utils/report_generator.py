def generate_report(match_score, resume_skills, jd_skills, missing_skills, tips):
    report = []
    report.append("📄 Resume vs JD Analyzer Report\n")
    report.append(f"Match Score: {match_score}%\n")

    report.append("✅ Extracted Resume Skills:")
    report.append(", ".join(sorted(resume_skills)) + "\n")

    report.append("📌 Required JD Skills:")
    report.append(", ".join(sorted(jd_skills)) + "\n")

    if missing_skills:
        report.append("❌ Missing Skills:")
        report.append(", ".join(sorted(missing_skills)) + "\n")

        report.append("💡 Suggested Improvements:")
        for tip in tips:
            report.append(f"- {tip}")
    else:
        report.append("✅ All required skills matched!")

    return "\n".join(report)
