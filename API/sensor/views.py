from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.core import serializers  
from django.views.decorators.csrf import csrf_exempt
from API import models
from API.scripts import error_response
import json

# Create your views here.

def sensor(request):
    sensorId = request.GET.get("id")
    
    if sensorId:
        if not models.sensor.objects.filter(id=sensorId):
            return error_response.throwError("Id de capteur introuvable")
        data = models.sensor.objects.filter(id=sensorId)
    else:
        data = models.sensor.objects.all().order_by('name')
    
    dataJson = serializers.serialize('json', data)
    return HttpResponse(dataJson, content_type='application/json', status=200)

def create(request):
    id = request.GET.get('id')
    name = request.GET.get('name')
    lat = request.GET.get('lat')
    lng = request.GET.get('lng')

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
    id = request.GET.get('id')

    try:
        sensor = models.sensor.objects.get(id=id)
    except:
        return error_response.bad_request('Id de capteur invalide')
    
    name = request.GET.get('name') or sensor.name
    lat = request.GET.get('lat') or sensor.lattitude
    lng = request.GET.get('lng') or sensor.longitude

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
    sensorId = request.GET.get('sensor_id')
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