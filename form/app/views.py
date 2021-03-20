from django.shortcuts import render
from rest_framework.response import Response
from .models import Pdf, Note, Phone, Sign
from .serializers import PdfSerializer, VoipSerializer, NoteSerializer, SignatureSerializer
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
            #return render(request, 'form.html', {'form' : serializer})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


from rest_framework.generics import ListAPIView,CreateAPIView

class NoteList(ListAPIView):
    queryset = Note.objects.values('note')
    serializer_class = NoteSerializer

class NoteCreate(CreateAPIView):
    queryset = Note.objects.values('note')
    serializer_class = NoteSerializer


from twilio.rest import Client

class Voip_api(APIView):

    def post(self, request,format=None):
        serializer = VoipSerializer(data = request.data)
        if serializer.is_valid():
            #breakpoint()
            #account_sid = os.environ['TWILIO_ACCOUNT_SID']
            #auth_token = os.environ['TWILIO_AUTH_TOKEN']
            account_sid = 'ACef24f2e76cd6000bf9aebaeb6e7a2256'
            auth_token = 'a0506cddf553fa104f9829200d804362'
            client = Client(account_sid, auth_token)

            call = client.calls.create(
                                    url='http://demo.twilio.com/docs/voice.xml',
                                    to= str(request.data['number']),
                                    #to='+919474040592',
                                    from_='+12143076206'
                                )

            print(call.sid)
            serializer.save()
            return Response({'msg':'calling... you '}, status=status.HTTP_201_CREATED)

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



