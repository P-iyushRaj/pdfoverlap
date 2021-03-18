
from rest_framework import serializers
from .models import Pdf

class PdfSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pdf
        fields = ['id','pdf_file', 'text', 'x', 'y']

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pdf
        fields = ['id','note']

class VoipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pdf
        fields = ['id','number']

class SignatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pdf
        fields = ['id','signature']