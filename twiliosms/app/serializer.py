from rest_framework import serializers
from .models import Voip

class VoipSerializer(serializers.ModelSerializer):
    class Meta :
        model = Voip
        fields = ['id', 'text']