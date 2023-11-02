from django.shortcuts import render
from rest_framework import generics
from .models import Note
from .serializers import *
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView


class NoteListCreateView(generics.ListCreateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializerAdd
    permission_classes = [IsAuthenticated]

   

    def perform_create(self, serializer):
        
        print(self.request.data)
        serializer.save(user=self.request.user)


class AllNotesListView(ListAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer