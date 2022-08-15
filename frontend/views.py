from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView

class Index(ListView):
    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, 'public_html/index.html',context)
