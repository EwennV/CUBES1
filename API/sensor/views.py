from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.core import serializers  
from django.views.decorators.csrf import csrf_exempt
from API import models
from API.scripts import error_response
import json

# Create your views here.

@csrf_exempt
def sensor(request):
    if not request.method == "GET":
        return error_response.bad_method()
    
    sensorId = request.GET.get("id")
    
    if sensorId:
        if not models.sensor.objects.filter(id=sensorId):
            return error_response.bad_request("Id de capteur introuvable")
        data = models.sensor.objects.filter(id=sensorId)
    else:
        data = models.sensor.objects.all().order_by('name')
    
    dataJson = serializers.serialize('json', data)
    return HttpResponse(dataJson, content_type='application/json', status=200)

@csrf_exempt
def create(request):
    if not request.method == "POST":
        return error_response.bad_method()
    body = (request.body).decode()

    try:
        data = json.loads(body)
    except:
        return error_response.bad_request("Données invalides.")

    id = data["id"]
    name = data["name"]
    lat = data["lat"]
    lng = data["lng"]

    if not id or not int(id):
        return error_response.bad_request('Id invalide')
      
    if models.sensor.objects.filter(id=id):
        return error_response.bad_request('Ce capteur est déjà enregistré')
    
    if not name or not str(name):
        return error_response.bad_request('Name invalide')
    
    if lat and not float(lat):
        return error_response.bad_request('Lattitude invalide')
    
    if lng and not float(lng):
        return error_response.bad_request('Longitude invalide')
    sensor = models.sensor(
        id = id,
        name = name,
        lattitude = lat,
        longitude = lng,
    )

    sensor.save()

    response = {
        'message': 'Capteur ajouté !'
    }
    
    return JsonResponse(response, status=200)
  
@csrf_exempt
def update(request):
    if not request.method == "PUT":
        return error_response.bad_method()
    
    body = (request.body).decode()

    try:
        data = json.loads(body)
    except:
        return error_response.bad_request("Données invalides.")

    if 'id' not in data:
        return error_response.bad_request("L'identifiant du capteur est requis.")

    id = data['id']

    try:
        sensor = models.sensor.objects.get(id=id)
    except:
        return error_response.bad_request('Id de capteur invalide')
    

    name = data["name"] or sensor.name
    lat = data["lat"] if "lat" in data else sensor.lattitude
    lng = data["lng"] if "lng" in data else sensor.longitude

    try:
        sensor.name = name
        sensor.lattitude = lat
        sensor.longitude = lng

        sensor.save()
    
    except ValueError:
        error_response.bad_request('Modifications impossibles')
        print(ValueError)

    response = {
        'message': "Capteur mis à jour !"
    }

    return JsonResponse(response, status=200)

@csrf_exempt
def delete(request):
    if not request.method == "DELETE":
        return error_response.bad_method()
    
    sensorId = request.GET.get('id')
    print(sensorId)
    if not sensorId:
        return error_response.bad_request("Id de capteur invalide")
    
    try:
        models.sensor.objects.get(id=sensorId).delete()
    except:
        return error_response.bad_request("Suppression impossible, l'id fourni doit être invalide.")
    
    response = {
        'message': 'Capteur supprimé'
    }
    return JsonResponse(response, status=200, content_type='application/json')