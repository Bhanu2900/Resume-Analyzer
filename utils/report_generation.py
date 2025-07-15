from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import io

def generate_pdf_report(match_score, resume_skills, jd_skills, missing_skills, tips):
    buffer = io.BytesIO()
    c = canvas.Canvas(buffer, pagesize=A4)
    width, height = A4
    y = height - 40

    def draw_line(text):
        nonlocal y
        if y < 40:  # start new page if near bottom
            c.showPage()
            y = height - 40
        c.drawString(40, y, text)
        y -= 20

    # Header
    draw_line("Resume vs Job Description Match Report")
    draw_line("-" * 80)
    draw_line(f"Match Score: {match_score}%")
    draw_line("")

    # Resume Skills
    draw_line("✅ Resume Skills:")
    for skill in sorted(resume_skills):
        draw_line(f"- {skill}")
    draw_line("")

    # JD Skills
    draw_line("📌 JD Required Skills:")
    for skill in sorted(jd_skills):
        draw_line(f"- {skill}")
    draw_line("")

    # Missing Skills
    if missing_skills:
        draw_line("❌ Missing Skills:")
        for skill in sorted(missing_skills):
            draw_line(f"- {skill}")
        draw_line("")

        draw_line("💡 Suggested Improvements:")
        for tip in tips:
            draw_line(f"- {tip}")
    else:
        draw_line("✅ Excellent! No missing skills.")

    c.save()
    buffer.seek(0)
    return buffer
