from django.db import models

# Create your models here.
class Stickynote(models.Model):
    note = models.CharField(max_length=50)