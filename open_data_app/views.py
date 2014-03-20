# Create your views here.

from django.http import HttpResponse
from open_data_app import models
from django.shortcuts import render

def index(request):
    return HttpResponse("Hello, world. You're at the index.")

def list(request):
    data_sets = models.dataset.objects.all()
    return render(request, 'list.html', {'datasets':data_sets})


