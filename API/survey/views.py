from django.shortcuts import render
from django.utils import timezone
from datetime import timedelta
from django.http import HttpResponse
from django.core import serializers
from API import models
from API.scripts import error_response
from datetime import datetime

# Create your views here.

# Fonction qui permet de lister par défaut les 100 derniers relevés

def list(request):
    # Possibilité d'ajouter des paramètres dans la requête pour affiner la recherche cf https://github.com/EwennV/CUBES1#utilisation-de-lapi
    idSensor = request.GET.get('id')
    limit = request.GET.get('limit','100')
    order = request.GET.get('order', 'desc')
    last = request.GET.get('last', None)

    try:
        limit = int(limit)
    except :
        return error_response.throw_error("Le paramètre limite est incorrect")
    
    maxLimit = 10000
    
    if limit > maxLimit:
        return error_response.throw_error(f"Le paramètre limite ne peut pas dépasser {maxLimit}")
    
    match order:
        case "asc":
            order = ''
        case "desc":
            order = "-"
        case _:
            return error_response.throw_error(f"Le paramètre order est invalide (asc, desc)")
        
    if idSensor:
        if not last:
            surveys = models.survey.objects.filter(sensor_id = idSensor).order_by(f'{order}date')[:limit]
        else:
            try:
                if not int(last) or not type(int(last)) is int:
                    raise ValueError()
            except ValueError:
                return error_response.throw_error("Le paramètre last est invalide (int)")

            differenceDate = timezone.localtime(timezone.now()) - timedelta(hours=int(last))
            surveys = models.survey.objects.filter(sensor_id = idSensor).filter(date__gte=differenceDate).order_by(f'{order}date')
        if not surveys:
            return error_response.throw_error('Aucun relevé pour ce capteur')
    else:
        surveys = models.survey.objects.order_by(f'{order}date')[:limit]
    
    surveysJson = serializers.serialize('json', surveys)

    return HttpResponse(surveysJson, status=200, content_type='application/json')
