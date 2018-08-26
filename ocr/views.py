from django.shortcuts import render
from django.views import generic
from .models import OcrDocument

# Create your views here.

class IndexView(generic.ListView):
    template_name = 'ocr/index.html'
    model = OcrDocument

class DocView(generic.DetailView):
    model = OcrDocument
