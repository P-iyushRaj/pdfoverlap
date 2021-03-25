
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Pdf(models.Model):
    pdf_file = models.FileField(upload_to='upload/')
    text = models.CharField(max_length=200 )
    x = models.IntegerField( )
    y = models.IntegerField( )
    page_no = models.IntegerField( null=True, blank =True )

class Note(models.Model):
    note = models.CharField(max_length=200 )

class Phone(models.Model):
    number = PhoneNumberField()

class Fax(models.Model):
    faxnumber = PhoneNumberField()
    fax_file = models.FileField(upload_to='faxed/' )

class Sign(models.Model):
    signature = models.ImageField(upload_to='upload/', null=True, blank =True )

