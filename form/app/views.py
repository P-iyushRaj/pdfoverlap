from django.shortcuts import render
from rest_framework.response import Response
from .models import Pdf, Note, Phone, Sign, Fax
from .serializers import PdfSerializer, VoipSerializer, NoteSerializer, SignatureSerializer, FaxSerializer, SignNowSerializer
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
            serializer.save()

            packet = io.BytesIO()
            can = canvas.Canvas(packet, pagesize=letter)
            can.drawString(int(request.data['x']), int(request.data['y']), str(request.data['text']))
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

#signnow
import requests

class SignNow_api(APIView):

    def post(self, request,format=None):
        serializer = SignNowSerializer(data = request.data)
        if serializer.is_valid():                
            url = "https://api-eval.signnow.com/document"
            ACCESS_KEY = str(settings.SIGNNOW_ACCESS_KEY)
            Bearer_api_key = 'Bearer ' + ACCESS_KEY
            headers = { 'Authorization':  Bearer_api_key ,}
            payload={}
            #breakpoint()
            attachments = [('file', (str(request.data['pdf_file_now']), request.data['pdf_file_now']),)]
            res = requests.request("POST", url, headers=headers, data=payload, files=attachments)
            response = json.loads(res.text)
            # print(res.text) #{"id":"4b0ad8f45a0f421bbb37aca57d748246c1176eb8"}
            #breakpoint()

            try:
                return Response({'msg':response['error']['message']}, status=status.HTTP_400_BAD_REQUEST)
            except:
                serializer.save(doc_id = str(response['id']))
                res2 = putfield(data = request.data, serializer=serializer, headers =headers)
                res3 = invitesigner( data = request.data, serializer=serializer, headers =headers )

                #breakpoint()
                return Response({'msg':'document uploaded on signnow + fields added + mailed to signer'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#signnowhtml form
import requests

class SignNowhtmlform_api(APIView):

    def get(self, request,format=None):
        ACCESS_KEY = str(settings.SIGNNOW_ACCESS_KEY)
        Bearer_api_key = 'Bearer ' + ACCESS_KEY
        headers = { 'Authorization':  Bearer_api_key ,}
        try:
            res1 = docupload(headers =headers)
            
            res2 = putfield(data = res1.data['data'], headers =headers)
            res3 = CreateSigningLink( data = res2.data['data'], headers =headers )
            #breakpoint()
            return Response({'msg':'document uploaded on signnow + fields added + mailed to signer', 'data':res3.data['data']}, status=status.HTTP_201_CREATED)
        except:
            return Response({'msg':"errors"}, status=status.HTTP_400_BAD_REQUEST)

import requests
def CreateSigningLink(data, headers):
    url = "https://api-eval.signnow.com/link"
    #breakpoint()
    payload=json.dumps({"document_id": str(data['id'])})
    res = requests.request("POST", url, headers=headers, data=payload)
    response = json.loads(res.text)
    #breakpoint()
    try:
        return Response({'msg':response['errors']['message']}, status=status.HTTP_400_BAD_REQUEST)
    except:
        return Response({'msg':'doc file uploaded signnow', 'data':response}, status=status.HTTP_201_CREATED)



def docupload(headers):
    
    url = "https://api-eval.signnow.com/document"
    payload={}
    attachments = [('file', ('check.docx', open("/Users/piyushraj/Desktop/pdfoverlap/form/Untitled document.docx" , 'rb')),)]
    res = requests.request("POST", url, headers=headers, data=payload, files=attachments)
    response = json.loads(res.text)
    #breakpoint()
    try:
        return Response({'msg':response['errors']['message']}, status=status.HTTP_400_BAD_REQUEST)
    except:
        return Response({'msg':'doc file uploaded signnow', 'data':response}, status=status.HTTP_201_CREATED)

def putfield( data, headers):
    #breakpoint()
    url = "https://api-eval.signnow.com/document/" + str(data['id'])
    payload_1={"fields": [{
            "x": 20,
            "y": 40,
            "width": 120,
            "height": 70,
            "page_number": 0,
            "label": "sign here",
            "role": "Signer 1",
            "required": True,
            "type": "signature",
        }]}
    payload = json.dumps(payload_1)
    res = requests.request("PUT", url, headers=headers, data=payload)
    response = json.loads(res.text)
    try:
        return Response({'msg':response['errors']['message']}, status=status.HTTP_400_BAD_REQUEST)
    except:
        return Response({'msg':'signature field added on signnow', 'data':response}, status=status.HTTP_201_CREATED)

def invitesigner( data, serializer, headers ):
    url = "https://api-eval.signnow.com/document/" + str(serializer.data['doc_id']) + "/invite"

    payload_1 = {
            "document_id": str(serializer.data['doc_id']),
            "subject": "piyushraj4598@gmail.com Needs Your Signature",
            "message": "piyushraj4598@gmail.com invited you to sign \"Request one signature\"",
            "from": "piyushraj4598@gmail.com",
            "to": [
                {
                "email": str(data['reciever_mailid']),
                "role_id": "34cc1705151a626d9a89ed93bb6c8c2979adffc8",
                "role": "Signer 1",
                "order": "1"
            }
        ]
        }
    
    payload = json.dumps(payload_1)
    response = requests.request("POST", url, headers=headers, data=payload)

    
    try:
        return Response({'msg':response['error']['message']}, status=status.HTTP_400_BAD_REQUEST)
    except:
        return Response({'msg':'signature field added on signnow', 'data':response}, status=status.HTTP_201_CREATED)





from django.http import HttpResponse
from django.shortcuts import render
import requests
from django.views.decorators.csrf import csrf_protect

@csrf_protect
def home(request):

    noteshistory = requests.get('http://127.0.0.1:8000/noteget/')
    notesdata = noteshistory.json()
    #print(notesdata)

    SignLinkres = requests.get('http://127.0.0.1:8000/SignNowhtml/')
    SignLink = SignLinkres.json()
    #print(SignLink['data']['url_no_signup'])

    #breakpoint()
    return render(request, 'home.html', context={'note':notesdata, 'sign_link':SignLink['data']['url_no_signup']})


