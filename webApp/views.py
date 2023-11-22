from django.shortcuts import render, redirect, get_object_or_404
import requests
# Create your views here

def home(request):
    return render(request, 'base.html')

def historique(request): 
    limite_releves =  request.GET.get('limite_releves', 1000)
    r = requests.get(f'http://localhost:8000/api/survey/list?limit={limite_releves}')
    data = {'data': r.json()} 
    return render(request, 'historique.html', data)

def dashboard(request):
    r = requests.get('http://localhost:8000/api/sensor')

    data = {
        'data': []
    }

    for sensor in r.json():
        try:
            r2 = requests.get(f'http://localhost:8000/api/survey/list?id={sensor["pk"]}&limit=1')
            r2 = r2.json()[0]

            data['data'].append({
                'sensor_id': sensor["pk"],
                'humidity': r2["fields"]["humidity"],
                'temperature': r2["fields"]["temperature"],
                'battery_level': r2["fields"]["battery_level"],
                'rssi': r2["fields"]["rssi"]
            })
        except:
            data['data'].append({
                'sensor_id': sensor["pk"],
                'humidity': "N/A",
                'temperature': "N/A",
                'battery_level': "N/A",
                'rssi': "N/A"
            })

    return render(request, 'dashboard.html', data)

def alerte(request):
    return render(request, 'alerte.html')

def carte(request):
    return render(request, 'carte.html')

def detail(request, sensorId):
    r = requests.get('http://localhost:8000/api/sensor')

    data = {
        'data': []
    }
    # print(sensorId)
    # print(r.json())
    r2 = requests.get(f'http://localhost:8000/api/survey/list?id={sensorId}&limit=1')
    print(f'http://localhost:8000/api/survey/list?id={sensorId}&limit=1')
    r2 = r2.json()[0]

    data['data'].append({
        'sensor_id': sensorId,
        'humidity': r2["fields"]["humidity"],
        'temperature': r2["fields"]["temperature"],
        'battery_level': r2["fields"]["battery_level"],
        'rssi': r2["fields"]["rssi"]
    })
    return render(request, 'detail.html', data)
