
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Pdf(models.Model):
    pdf_file = models.FileField(upload_to='upload/')
    text = models.CharField(max_length=200 )
    x = models.IntegerField( )
    y = models.IntegerField( )
    page_no = models.IntegerField( null=True, blank =True )

    objects = models.Manager()

class Note(models.Model):
    note = models.CharField(max_length=200 )
    objects = models.Manager()

class Phone(models.Model):
    number = PhoneNumberField()
    objects = models.Manager()

class Fax(models.Model):
    faxnumber = PhoneNumberField()
    fax_file = models.FileField(upload_to='faxed/' )
    objects = models.Manager()

class htmlformsign(models.Model):
    name = models.CharField(max_length=200 , null=True, blank =True )
    mobilenum = PhoneNumberField( null=True, blank =True )

    objects = models.Manager()

#number identification

