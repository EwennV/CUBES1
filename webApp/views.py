from django.shortcuts import render
import requests
# Create your views here

def home(request):
    return render(request, 'dashboard.html')

def historique(request): 
    r = requests.get("http://localhost:8000/api/survey/list?limit=10")
    context = {'data': r.json()}

    return render(request, 'historique.html', context)

def dashboard(request):
    return render(request, 'dashboard.html')

def alerte(request):
    return render(request, 'alerte.html')

def carte(request):
    return render(request, 'carte.html')

def capteur(request, sensorId):
    r = requests.get('http://localhost:8000/api/sensor?id=',sensorId)
    context = {'sensor': r.json()[0]}

    return render(request, 'capteur.html', context)