from django.shortcuts import render
from .models import Note
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import Notes

@api_view(['GET'])
def get_notes(request):
    notes=Note.objects.all()
    serializer=Notes(notes,many=True)
    return Response(serializer.data)
