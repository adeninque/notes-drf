from django.shortcuts import render
from rest_framework import viewsets, mixins
from rest_framework.response import Response
from rest_framework.request import Request

from .models import Note
from .serializers import NoteSerializer

# Create your views here.
class NoteViewset(mixins.RetrieveModelMixin,
                  mixins.ListModelMixin,
                  mixins.DestroyModelMixin,
                  mixins.UpdateModelMixin,
                  viewsets.GenericViewSet):
  queryset = Note.objects.all()
  serializer_class = NoteSerializer
  
  def post(self, request: Request):
    serializer = NoteSerializer(data = request.data)
    serializer.is_valid(raise_exception = True)
    serializer.save(author = request.user)
        
    return Response(serializer.data)