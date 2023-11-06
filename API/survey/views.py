from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from API import models
from API.scripts import error_response

# Create your views here.

# Fonction qui permet de lister par défaut les 100 derniers relevés

def list(request):
    # Possibilité d'ajouter des paramètres dans la requête pour affiner la recherche cf https://github.com/EwennV/CUBES1#utilisation-de-lapi
    idSensor = request.GET.get('id')
    limit = request.GET.get('limit','100')
    order = request.GET.get('order', 'desc')

    try:
        limit = int(limit)
    except :
        return error_response.throwError("Le paramètre limite est incorrect")
    
    maxLimit = 10000
    
    if limit > maxLimit:
        return error_response.throwError(f"Le paramètre limite ne peut pas dépasser {maxLimit}")
    
    match order:
        case "asc":
            order = ''
        case "desc":
            order = "-"
        case _:
            return error_response.throwError(f"Le paramètre order est invalide (asc, desc)")
        
    if idSensor:
        surveys = models.survey.objects.filter(sensor_id = idSensor).order_by(f'{order}date')[:limit]
        if not surveys:
            return error_response.throwError('id de capteur introuvable')
    else:
        surveys = models.survey.objects.order_by(f'{order}date')[:limit]
    
    
    surveysJson = serializers.serialize('json', surveys)
    return HttpResponse(surveysJson, status=200, content_type='application/json')
