from rest_framework import serializers
from .models import Pdf

class PdfSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pdf
        fields = ['pdf_file']
