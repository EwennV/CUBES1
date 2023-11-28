from django.shortcuts import render
from datetime import datetime
from django.urls import reverse
import requests
# Create your views here

def home(request):
    return render(request, 'base.html')

def historique(request): 
    limite_releves =  request.GET.get('limite_releves', 1000)
    print(f'http://{request.get_host()}{reverse("api_survey:api_survey_list")}/api/survey/list?limit={limite_releves}')
    r = requests.get(f'http://{request.get_host()}{reverse("api_survey:api_survey_list")}?limit={limite_releves}')
    data = {'data': r.json()} 
    return render(request, 'historique.html', data)

def dashboard(request):
    r = requests.get(f'http://{request.get_host()}{reverse("api_sensor:api_sensor_list")}')

    data = {
        'data': []
    }

    for sensor in r.json():
        try:
            r2 = requests.get(f'http://{request.get_host()}{reverse("api_survey:api_survey_list")}?id={sensor["pk"]}&limit=1')
            r2 = r2.json()[0]

            data['data'].append({
                'sensor_id': sensor["pk"],
                'name': sensor["fields"]["name"],
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
    data = {}
    
    r = requests.get(f'http://localhost:8000/api/sensor?id={sensorId}')

    sensor = r.json()[0]
    
    nom_capteur = sensor['fields']['name']

    r2 = requests.get(f'http://localhost:8000/api/survey/list?id={sensorId}&limit=1')
    r2 = r2.json()[0]

    data['data']= {
        'sensor_id': sensorId,
        'nom': nom_capteur,
        'humidity': r2["fields"]["humidity"],
        'temperature': r2["fields"]["temperature"],
        'battery_level': r2["fields"]["battery_level"],
        'rssi': r2["fields"]["rssi"]
    }
    
    graph_data = {
        'labels': [],  # Liste pour les dates
        'clean_date': [],
        'temperature_data': [],  # Liste pour les températures
        'humidity_data': []  # Liste pour les humidités
    }

    r3 = requests.get(f'http://{request.get_host()}{reverse("api_survey:api_survey_list")}?id={sensorId}&last=24')

    surveys = r3.json()

    for survey in surveys:
        graph_data['labels'].append(survey["fields"]["date"])
        datetime_object = datetime.strptime(survey["fields"]["date"], '%Y-%m-%dT%H:%M:%SZ')
        heure = datetime_object.strftime('%d/%m - %H:%M')
        graph_data['clean_date'].append(heure)
        graph_data['temperature_data'].append(survey["fields"]["temperature"])
        graph_data['humidity_data'].append(survey["fields"]["humidity"])

    data['graph_data'] = graph_data

    return render(request, 'detail.html', data)

def modification(request, sensorId):
    data = {}
    
    r = requests.get(f'http://localhost:8000/api/sensor?id={sensorId}')

    sensor = r.json()[0]
    
    nom_capteur = sensor['fields']['name']

    r2 = requests.get(f'http://localhost:8000/api/survey/list?id={sensorId}&limit=1')
    r2 = r2.json()[0]

    data['data']= {
        'sensor_id': sensorId,
        'nom': nom_capteur,
    }
    return render(request, 'modification.html', data)

def ajout(request):
    return render(request, 'ajout.html')