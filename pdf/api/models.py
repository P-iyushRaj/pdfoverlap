from django.db import models

# Create your models here.
class Pdf(models.Model):
    pdf_file = models.FileField(upload_to='upload/',  null=True, blank =True, )
