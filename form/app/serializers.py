
from rest_framework import serializers
from .models import Pdf, Note, Phone, Sign, Fax

class PdfSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pdf
        fields = ['id','pdf_file','page_no', 'text', 'x', 'y']

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ['id','note']

class VoipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phone
        fields = ['id','number']


class FaxSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fax
        fields = ['id','faxnumber', 'fax_file']

class SignatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sign
        fields = ['id','signature']