from django.shortcuts import render
import requests
import models
# Create your views here

def home(request):
    return render(request, 'base.html')

def historique(request): 
    requests.get('/api/survey/list')
    data = [
        {'sensor_id': 'name', 'date': 'date': 'temperature':'temperature', 'humidity':'humidity'}
    ]
    return render(request, 'historique.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def alerte(request):
    return render(request, 'alerte.html')

def carte(request):
    return render(request, 'carte.html')

def detail(request):
    return render(request, 'detail.html')