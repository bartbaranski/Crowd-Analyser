from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def generate_pdf_report(file_path, total_people, avg_people_per_minute):
    c = canvas.Canvas(file_path, pagesize=letter)
    c.drawString(100, 750, "Raport z analizy wideo")
    c.drawString(100, 725, f"Liczba uczestników: {total_people}")
    c.drawString(100, 700, f"Średnia liczba osób na minutę: {avg_people_per_minute:.2f}")
    c.save()
