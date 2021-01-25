from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from .serializers import MessageSerializer
from .models import Messages
# Create your views here.
class base(generics.ListCreateAPIView):
    queryset = Messages.objects.all()
    serializer_class = MessageSerializer
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)