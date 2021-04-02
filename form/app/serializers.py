
from rest_framework import serializers
from .models import Pdf, Note, Phone, Sign, Fax, SignNow, htmlformsign

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

class SignNowSerializer(serializers.ModelSerializer):

    class Meta:
        model = SignNow
        fields = ['id','pdf_file_now', 'doc_id']

        extra_kwargs = {'pdf_file_now': {'required': True, 'allow_null': False}}
        #extra_kwargs = {'doc_id': {'required': True, 'allow_null': False}}

class SignNowFieldputSerializer(serializers.ModelSerializer):

    class Meta:
        model = SignNow
        #fields = ['id','pdf_file_now', 'doc_id', 'x_s', 'y_s',  'page_number','x_t', 'y_t',  'page_number_t', 'reciever_mailid']
        fields = ['id','pdf_file_now', 'reciever_mailid']

        extra_kwargs = {'pdf_file_now': {'required': True, 'allow_null': False}}
        #extra_kwargs = {'doc_id': {'required': True, 'allow_null': False}}

                
class SignatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = htmlformsign
        fields = ['id','name']
        
