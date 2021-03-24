
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class Pdf(models.Model):
    pdf_file = models.FileField(upload_to='upload/')
    text = models.CharField(max_length=200 )
    x = models.IntegerField( )
    y = models.IntegerField( )
    page_no = models.IntegerField( null=True, blank =True )

class Note(models.Model):
    note = models.CharField(max_length=200 )


class Phone(models.Model):

    #number = models.IntegerField(max_length=919474040592, null=True, blank =True )
    number = PhoneNumberField( null=True, blank =True )
    #number = PhoneField(blank=True, null = True, help_text='Contact phone number')

class Fax(models.Model):

    #number = models.IntegerField(max_length=919474040592, null=True, blank =True )
    number = PhoneNumberField( null=True, blank =True )
    #number = PhoneField(blank=True, null = True, help_text='Contact phone number')

class Sign(models.Model):

    signature = models.ImageField(upload_to='upload/', null=True, blank =True )

