from django.shortcuts import render
from datetime import datetime
from django.urls import reverse
import requests
from django.http import HttpResponseNotFound
# Create your views here

def home(request):
    return render(request, 'base.html')

def historique(request): 
    limite_releves =  request.GET.get('limite_releves', 1000)
    r = requests.get(f'http://{request.get_host()}/api/survey/list?limit={limite_releves}')
    data = {'data': r.json()}
    print(data)
    return render(request, 'historique.html', data)

def dashboard(request):
    sensors = requests.get(f'http://{request.get_host()}/api/sensor')

    data = {
        'data': []
    }

    for sensor in sensors.json():
        survey_request = requests.get(f'http://{request.get_host()}/api/survey/list?id={sensor["pk"]}&limit=1')

        last_survey = None

        if (survey_request.status_code == 200):
            last_survey = survey_request.json()[0]

        data['data'].append({
            'sensor_id': sensor["pk"],
            'name': sensor["fields"]["name"],
            'humidity': last_survey["fields"]["humidity"] if last_survey else "N/A",
            'temperature': last_survey["fields"]["temperature"] if last_survey else "N/A",
            'battery_level': last_survey["fields"]["battery_level"] if last_survey else "N/A",
            'rssi': last_survey["fields"]["rssi"] if last_survey else "N/A",
            'isActive': sensor['fields']['isActive']
        })

    return render(request, 'dashboard.html', data)

def dashboardAlerte(request):
    alerts = requests.get(f'http://{request.get_host()}/api/alert')

    if not alerts.status_code == 200:
        raise HttpResponseNotFound('Alerts not found')
    context = {
        "alerts": alerts.json()
    }
    return render(request, 'dashboardAlerte.html', context)

def carte(request):
    return render(request, 'carte.html')

def detail(request, sensorId):
    data = {}
    
    r = requests.get(f'http://{request.get_host()}/api/sensor?id={sensorId}')

    if not r.status_code == 200:
        raise HttpResponseNotFound("Sensor not found")
    
    sensor = r.json()[0]

    r2 = requests.get(f'http://{request.get_host()}/api/survey/list?id={sensorId}&last=24')

    surveys = r2.json()
    last_survey = None

    if (r2.status_code == 200):
        last_survey = surveys[0]
    
    data['data'] = {
        'sensor_id': sensorId,
        'nom': sensor['fields']['name'],
        'humidity': last_survey["fields"]["humidity"] if last_survey else "N/A",
        'temperature': last_survey["fields"]["temperature"] if last_survey else "N/A",
        'battery_level': last_survey["fields"]["battery_level"] if last_survey else "N/A",
        'rssi': last_survey["fields"]["rssi"] if last_survey else "N/A"
    }

    if (last_survey):
    
        graph_data = {
            'labels': [],  # Liste pour les dates
            'clean_date': [],
            'temperature_data': [],  # Liste pour les températures
            'humidity_data': []  # Liste pour les humidités
        }

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
    
    r = requests.get(f'http://{request.get_host()}/api/sensor?id={sensorId}')

    if not r.status_code == 200:
        return HttpResponseNotFound("Sensor not found")

    sensor = r.json()[0]

    data['data']= {
        'sensor_id': sensorId,
        'nom': sensor['fields']['name'],
    }
    return render(request, 'modification.html', data)


def ajout(request):
    return render(request, 'ajout.html')


def ajoutAlerte(request):
    return render(request, 'ajoutAlerte.html')


def modifAlerte(request, alertId):
    alertRequest = requests.get(f'http://{request.get_host()}/api/alert?id={alertId}')

    if not alertRequest.status_code == 200:
        raise HttpResponseNotFound('Alerts not found')

    context = {
        "alert": alertRequest.json()[0]
    }
    return render(request, 'modifAlerte.html', context)