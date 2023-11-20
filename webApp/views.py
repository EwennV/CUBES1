from django.shortcuts import render
import requests
# Create your views here

def home(request):
    return render(request, 'dashboard.html')

def historique(request): 
    r = requests.get("http://localhost:8000/api/survey/list?limit=10")
    data = {'data': r.json()}

    return render(request, 'historique.html', data)

def dashboard(request):
    return render(request, 'dashboard.html')

def alerte(request):
    return render(request, 'alerte.html')

def carte(request):
    return render(request, 'carte.html')

def detail(request):
    return render(request, 'detail.html')