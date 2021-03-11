from rest_framework import serializers
from .models import Stickynote

class StickynoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stickynote
        fields = [ 'note']