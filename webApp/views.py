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
