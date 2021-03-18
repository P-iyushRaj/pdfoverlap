
from django.contrib import admin

# Register your models here.
from .models import Pdf

@admin.register(Pdf)
class PdfAdmin(admin.ModelAdmin):
    list_display = ['id']

    