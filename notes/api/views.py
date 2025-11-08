from django.shortcuts import render
from .models import Note
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserRegisterSerializer,NoteSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser
from .models import User

class RegistrationAPIView(generics.CreateAPIView):
    queryset=User.objects.all()
    permission_classes=[AllowAny]
    serializer_class=UserRegisterSerializer

class CreateListAPIView(generics.ListCreateAPIView):
    serializer_class=NoteSerializer
    permission_classes=[IsAuthenticated]
    
    def get_queryset(self):
        return Note.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)
    

class NoteDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class=NoteSerializer
    permission_classes=[IsAuthenticated]

    def get_queryset(self):
        return Note.objects.filter(user=self.request.user)    
    

    
    
        
    

