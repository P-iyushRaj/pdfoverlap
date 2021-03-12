from PyPDF2 import PdfFileWriter, PdfFileReader
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
packet = io.BytesIO()
can = canvas.Canvas(packet, pagesize=letter)
can.drawString(200, 800, "Hello world again")
can.save()
packet.seek(0)
new_pdf = PdfFileReader(packet)
existing_pdf = PdfFileReader(open("destination10.pdf", "rb"))
output = PdfFileWriter()
page = existing_pdf.getPage(0)
page.mergePage(new_pdf.getPage(0))
output.addPage(page)
outputStream = open("destination11.pdf", "wb")
output.write(outputStream)
outputStream.close()
