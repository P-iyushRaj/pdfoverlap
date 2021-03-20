
from django.contrib import admin

# Register your models here.
from .models import Pdf, Note, Phone, Sign

@admin.register(Pdf)
class PdfAdmin(admin.ModelAdmin):
    list_display = ['id', 'text']

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ['id', 'note']

@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    list_display = ['id', 'number']

@admin.register(Sign)
class SignAdmin(admin.ModelAdmin):
    list_display = ['id', 'signature']