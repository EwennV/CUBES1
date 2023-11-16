from django.shortcuts import render
# Create your views here

def home(request):
    return render(request, 'base.html')

def historique(request): 
    data = [
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