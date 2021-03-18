
from django.db import models

# Create your models here.
class Pdf(models.Model):
    pdf_file = models.FileField(upload_to='upload/',  null=True, blank =True )
    text = models.CharField(max_length=200,  null=True, blank =True )
    x = models.IntegerField( null=True, blank =True )
    y = models.IntegerField( null=True, blank =True )

    note = models.CharField(max_length=200,  null=True, blank =True )

    number = models.IntegerField( null=True, blank =True )

    signature = models.ImageField(upload_to='upload/', null=True, blank =True )

