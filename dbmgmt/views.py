from django.shortcuts import render
from .serializers import ContactFormSerializer
from .models import ContactForm
from rest_framework import viewsets
# Create your views here.
class ContactFieldView(viewsets.ModelViewSet):
    serializer_class = ContactFormSerializer
    queryset = ContactForm.objects.all()
