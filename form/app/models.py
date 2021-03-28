
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

class Sign(models.Model):
    signature = models.ImageField(upload_to='upload/', null=True, blank =True )

    objects = models.Manager()

type_choice = (
    ("T", "text"),
    ("S", "signature")
)

class SignNow(models.Model):
    pdf_file_now = models.FileField(upload_to='uploadsignnow/' ,null=True, blank =True )
    doc_id = models.CharField(max_length=500, null=True, blank =True )

    x_s = models.IntegerField( null=True, blank =True )
    y_s = models.IntegerField( null=True, blank =True )
    #label = models.CharField(max_length=100, null=True, blank =True )
    #types = models.CharField(choices=type_choice, max_length=100, null=True, blank =True )
    page_number = models.IntegerField(null=True, blank =True )

    reciever_mailid = models.EmailField(max_length=2540, null=True, blank =True )

    objects = models.Manager()


