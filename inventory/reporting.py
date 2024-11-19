from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def generate_pdf(data, filename="static/inventory_report.pdf"):
    c = canvas.Canvas(filename, pagesize=letter)
    c.setFont("Helvetica", 12)
    c.drawString(100, 750, "Inventory Report")
    c.drawString(100, 730, "------------------------------")

    y = 700
    for row in data:
        c.drawString(100, y, f"Serial: {row[1]}, Item: {row[2]}, Price: {row[3]}, Quantity: {row[4]}")
        y -= 20

    c.save()
