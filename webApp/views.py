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
    r = requests.get('http://localhost:8000/api/sensor')

    truc = {
        'data': []
    }

    for sensor in r.json():
        r2 = requests.get(f'http://localhost:8000/api/survey/list?id={sensor["pk"]}&limit=1')
        r2 = r2.json()[0]
        truc['data'].append({
            'sensor_id': sensor["pk"],
            'humidity': r2["fields"]["humidity"],
            'temperature': r2["fields"]["temperature"],
            'battery_level': r2["fields"]["battery_level"],
            'rssi': r2["fields"]["rssi"]
        })
    print(truc)
    return render(request, 'dashboard.html', truc)

def alerte(request):
    return render(request, 'alerte.html')

def carte(request):
    return render(request, 'carte.html')

def capteur(request, sensorId):
    r = requests.get('http://localhost:8000/api/sensor?id=',sensorId)
    context = {'sensor': r.json()[0]}

    return render(request, 'capteur.html', context)