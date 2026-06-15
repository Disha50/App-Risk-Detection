from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import io

def generate_pdf(data):
    buffer = io.BytesIO()
    pdf = canvas.Canvas(buffer, pagesize=letter)

    pdf.setFont("Helvetica-Bold", 18)
    pdf.drawString(100, 750, "AI Application Risk Report")

    pdf.setFont("Helvetica", 12)
    pdf.drawString(100, 710, f"App Name: {data['app']}")
    pdf.drawString(100, 680, f"Risk Score: {data['risk_score']}")
    pdf.drawString(100, 650, f"AI Confidence: {data['ai_confidence']}")

    pdf.drawString(100, 610, "Detected Issues:")
    y = 590
    for issue in data["issues"]:
        pdf.drawString(120, y, f"- {issue}")
        y -= 20

    pdf.drawString(100, y - 10, "Recommended Solutions:")
    y -= 30
    for sol in data["solutions"]:
        pdf.drawString(120, y, f"- {sol}")
        y -= 20

    pdf.save()
    buffer.seek(0)
    return buffer
