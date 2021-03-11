from django.shortcuts import render

# Create your views here.
from .models import Stickynote
from .serializer import StickynoteSerializer

from rest_framework.generics import ListAPIView,CreateAPIView

class NoteList(ListAPIView):
    queryset = Stickynote.objects.all()
    serializer_class = StickynoteSerializer

class NoteCreate(CreateAPIView):
    queryset = Stickynote.objects.all()
    serializer_class = StickynoteSerializer

