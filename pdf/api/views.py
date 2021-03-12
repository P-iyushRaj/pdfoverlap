 
from django.shortcuts import render
from rest_framework.response import Response
from .models import Pdf
from .serializer import PdfSerializer
from rest_framework import status
from rest_framework.views import APIView

from PyPDF2 import PdfFileWriter, PdfFileReader
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

class Pdf_api(APIView):

    def post(self, request,format=None):
        serializer = PdfSerializer(data = request.data)
        if serializer.is_valid():

            #import pdb; pdb.set_trace()
            #print(serializer.validated_data)

            serializer.save()

            packet = io.BytesIO()
            can = canvas.Canvas(packet, pagesize=letter)
            can.drawString(200, 460, "HELLO PIYUSH RAJ")
            can.drawString(200, 420, "MANTRA LABS")
            can.save()
            packet.seek(0)

            #import pdb; pdb.set_trace()
            new_pdf = PdfFileReader(packet)
            #path = "media/upload/destination10.pdf"
            pdf_path = "media/upload/" + str(request.data['pdf_file'])
            pdffile = open(pdf_path, "rb")
            existing_pdf = PdfFileReader(pdffile)

            #print(request.data['pdf_file'])
            output = PdfFileWriter()
            page = existing_pdf.getPage(0)
            page.mergePage(new_pdf.getPage(0))
            #import pdb; pdb.set_trace()
            output.addPage(page)
            pdfmodified_path = "./media/result/" + str(request.data['pdf_file'])
            outputStream = open(pdfmodified_path, "wb")
            output.write(outputStream)            
            outputStream.close()

            return Response({'msg':'data created', "data":pdfmodified_path}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

