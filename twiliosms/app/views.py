from django.shortcuts import render
from rest_framework.response import Response
from .models import Voip
from .serializer import VoipSerializer
from rest_framework import status
from rest_framework.views import APIView

from twilio.rest import Client


class Voip_api(APIView):

    def post(self, request,format=None):
        serializer = VoipSerializer(data = request.data)
        if serializer.is_valid():
            #breakpoint()
            if str(request.data['text']) == 'sms':
                #account_sid = os.environ['TWILIO_ACCOUNT_SID']
                #auth_token = os.environ['TWILIO_AUTH_TOKEN']
                account_sid = 'ACef24f2e76cd6000bf9aebaeb6e7a2256'
                auth_token = '1f8adc50ca6e40dab739c903f8dc6754'
                client = Client(account_sid, auth_token)

                message = client.messages \
                                .create(
                                    body= f"the text was : {str(request.data['text'])}",
                                    from_='+12143076206',
                                    to='+919474040592'
                                )

                print(message.sid)
                serializer.save()
                return Response({'msg':'sms sent, check your phone'}, status=status.HTTP_201_CREATED)

            if str(request.data['text']) == 'voice':
                #account_sid = os.environ['TWILIO_ACCOUNT_SID']
                #auth_token = os.environ['TWILIO_AUTH_TOKEN']
                account_sid = 'ACef24f2e76cd6000bf9aebaeb6e7a2256'
                auth_token = '1f8adc50ca6e40dab739c903f8dc6754'
                client = Client(account_sid, auth_token)

                call = client.calls.create(
                                        url='http://demo.twilio.com/docs/voice.xml',
                                        to='+919474040592',
                                        from_='+12143076206'
                                    )

                print(call.sid)
                serializer.save()
                return Response({'msg':'calling... you '}, status=status.HTTP_201_CREATED)


        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

