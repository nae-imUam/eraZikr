from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def Home(request):
    return render(request, 'ezikr/home.html')

def Next(request):
    return render(request, 'ezikr/base.html')
