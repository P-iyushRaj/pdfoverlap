from django.db import models
import os
from twilio.rest import Client


# Create your models here.
class Voip(models.Model):
    text = models.CharField(max_length=50)

    def __str__(self):
        return str(self.text)

'''
    def save(self, *args , **kwargs):
        if self.text == 'sms':
            #account_sid = os.environ['TWILIO_ACCOUNT_SID']
            #auth_token = os.environ['TWILIO_AUTH_TOKEN']
            account_sid = 'ACef24f2e76cd6000bf9aebaeb6e7a2256'
            auth_token = '1f8adc50ca6e40dab739c903f8dc6754'
            client = Client(account_sid, auth_token)

            message = client.messages \
                            .create(
                                body= f"the text was : {self.text}",
                                from_='+12143076206',
                                to='+919474040592'
                            )

            print(message.sid)

        return super().save(*args, **kwargs)
'''