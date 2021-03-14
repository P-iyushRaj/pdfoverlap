from django.contrib import admin

# Register your models here.
from .models import Voip

@admin.register(Voip)
class VoipAdmin(admin.ModelAdmin):
    list_display = ['id', 'text']
