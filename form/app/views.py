from django.shortcuts import render
from rest_framework.response import Response
from .models import Pdf, Note, Phone, Sign, Fax
from .serializers import PdfSerializer, VoipSerializer, NoteSerializer, SignatureSerializer, FaxSerializer
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
            serializer.save()

            packet = io.BytesIO()
            can = canvas.Canvas(packet, pagesize=letter)
            can.drawString(int(request.data['x']), int(request.data['x']), str(request.data['text']))
            #can.drawString(200, 420, "MANTRA LABS")
            can.save()
            packet.seek(0)
            #breakpoint()

            #import pdb; pdb.set_trace()
            new_pdf = PdfFileReader(packet)
            #path = "media/upload/destination10.pdf"
            pdf_path = "media/upload/" + str(request.data['pdf_file'])
            pdffile = open(pdf_path, "rb")
            existing_pdf = PdfFileReader(pdffile)

            output = PdfFileWriter()
            #breakpoint()
            page = existing_pdf.getPage(int(request.data['page_no']))
            #page = existing_pdf.getPage(0)
            page.mergePage(new_pdf.getPage(0))
            output.addPage(page)
            pdfmodified_path = "./media/result/" + str(request.data['pdf_file'])
            outputStream = open(pdfmodified_path, "wb")
            output.write(outputStream)            
            outputStream.close()
            #breakpoint()
            pdf_writer = PdfFileWriter()
            for page in range(existing_pdf.getNumPages()):
                current_page = existing_pdf.getPage(page)
                if page == int(request.data['page_no']):
                    updated_pdf_path = "media/result/" + str(request.data['pdf_file'])
                    updatedpdffile = open(updated_pdf_path, "rb")
                    modified_pdf = PdfFileReader(updatedpdffile)
                    pdf_writer.addPage(modified_pdf.getPage(0))
                else:
                    pdf_writer.addPage(current_page)
            output_filename = "./media/finalresult/" + str(request.data['pdf_file'])
            #breakpoint()
            with open(output_filename, "wb") as out:
                pdf_writer.write(out)
            return Response({'msg':'data created', "data":output_filename}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


from rest_framework.generics import ListAPIView,CreateAPIView

class NoteList(ListAPIView):
    queryset = Note.objects.values('note')
    serializer_class = NoteSerializer

class NoteCreate(CreateAPIView):
    queryset = Note.objects.values('note')
    serializer_class = NoteSerializer


from twilio.rest import Client
import os
from django.conf import settings

class Voip_api(APIView):

    def post(self, request,format=None):
        serializer = VoipSerializer(data = request.data)
        if serializer.is_valid():
            #account_sid = os.environ['TWILIO_ACCOUNT_SID']
            #auth_token = os.environ['TWILIO_AUTH_TOKEN']
            #from_num = os.environ['FROM_TWILIO_NUMBER']
            account_sid = settings.TWILIO_ACCOUNT_SID
            auth_token = settings.TWILIO_AUTH_TOKEN
            from_num = settings.FROM_TWILIO_NUMBER
            client = Client(account_sid, auth_token)

            call = client.calls.create(
                                    url='http://demo.twilio.com/docs/voice.xml',
                                    to= str(request.data['number']),
                                    #to='+919474040592',
                                    from_= from_num)
            #print(call.sid)
            serializer.save()
            return Response({'msg':'calling... you '}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#https://app.documo.com/fax/history
#https://docs.documo.com/?python#send-multiple-faxes
#https://support.twilio.com/hc/en-us/articles/1260800821230-Programmable-Fax-Migration-Guide-for-Documo-mFax

import requests
import json

class Fax_api(APIView):

    def post(self, request,format=None):
        serializer = FaxSerializer(data = request.data)
        if serializer.is_valid():
                        
            url = "https://api.documo.com/v1/faxes"
            API_KEY = str(settings.DOCUMO_API_KEY)
            Basic_api_key = 'Basic ' + API_KEY
            headers = { 'Authorization':  Basic_api_key ,}
            #breakpoint()
            data = [
            ('faxNumber', str(request.data['faxnumber'])),
            ('coverPage', 'false'),
            ('recipientName', 'John'),
            ('subject', 'test'),
            ('notes', 'test'),
            ('tags', '4c225812-81f1-4827-8194-b0e9475c54e6'),
            ('cf', '{"patientID":"1234"}'),]
            #breakpoint()
            #attachments = [('file', ('check.png', open(file_path , 'rb'), 'application/png'),)]
            attachments = [('file', ('check.png', request.data['fax_file']),)]
            res = requests.post(url, headers=headers, data=data, files=attachments)
            response = json.loads(res.text)

            try:
                return Response({'msg':response['error']['message']}, status=status.HTTP_400_BAD_REQUEST)
            except:
                serializer.save()
                return Response({'msg':'fax sent'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Sign_api(CreateAPIView):
    queryset = Sign.objects.values('signature')
    serializer_class = SignatureSerializer


from django.http import HttpResponse
from django.shortcuts import render
import requests
from django.views.decorators.csrf import csrf_protect

@csrf_protect
def home(request):

    noteshistory = requests.get('http://127.0.0.1:8000/noteget/')
    notesdata = noteshistory.json()

    #breakpoint()
    return render(request, 'home.html', context={'note':notesdata,})



