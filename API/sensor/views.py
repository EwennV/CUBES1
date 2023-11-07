from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers  
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
    data = {
        'name': 'John Doe',
        'age': 30,
        'email': 'john.doe@example.com'
    }
    return HttpResponse(data, status=200, content_type="application/json")

def update(request):
    data = {
        'name': 'John Doe',
        'age': 30,
        'email': 'john.doe@example.com'
    }
    return HttpResponse(data, status=200, content_type='application/json')