from django.contrib import admin

# Register your models here.
from .models import Stickynote

@admin.register(Stickynote)
class StickynoteAdmin(admin.ModelAdmin):
    list_display = ['note']