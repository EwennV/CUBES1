from django.shortcuts import render
import requests
# Create your views here

def home(request):
    return render(request, 'sensors/list.html')


def historique(request):
   
    response = requests.get('/api/survey/list')
    data = response.json()  

    return render(request, 'base.html', {'data': data})