from django.shortcuts import render
from .models import *
# Create your views here.

def Home(request):
    tasks = Task.objects.all()
    challanges = Challange.objects.all()
    context = {
        'tasks':tasks,
        'challanges':challanges
    }
    return render(request, 'ezikr/home.html', context)

def Next(request, task_id):
    task = Task.objects.get(id=task_id)
    context = {
        'task':task
    }
    return render(request, 'ezikr/zikra.html', context)

def Certify(request):
    return render(request, 'ezikr/certify.html')
