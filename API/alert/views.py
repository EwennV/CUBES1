from django.http import JsonResponse
from django.http import HttpResponse
from API.models import alert, recipient
from django.core import serializers  
from API.scripts import error_response
import json
from django.views.decorators.csrf import csrf_exempt

def list(request):
    if not request.method == "GET":
        return error_response.bad_method()
    
    alertId = request.GET.get('id')

    if alertId:
        if not alert.objects.filter(id=alertId):
            return error_response.bad_request('Alerte introuvable')
        data = alert.objects.filter(id=alertId)
    else:
        data = alert.objects.all()

    data_json = serializers.serialize('json', data)
    return HttpResponse(data_json, content_type="application/json", status=200)

@csrf_exempt
def create(request):
    if not request.method == "POST":
        return error_response.bad_method()
    
    body = (request.body).decode()

    try:
        body = json.loads(body)
        frequency = body.get("frequency")
    except:
        return error_response.bad_request("Erreur de syntaxe des données transmises")
    
    try:
        recipients = body['recipients']
    except:
        return error_response.bad_request("Aucun destinataire")

    try:
        temperature_superior = float(body.get('temperature_superior', 0))
        temperature_inferior = float(body.get('temperature_inferior', 0))
        humidity_superior = int(body.get('humidity_superior', 0))
        humidity_inferior = int(body.get('humidity_inferior', 0))
    except ValueError:
        return error_response.bad_request("Valeurs de température ou d'humidité invalides")

    new_alert = alert()

    new_alert.frequency = frequency
    
    new_alert.temperature_superior = int(temperature_superior)
    new_alert.temperature_inferior = int(temperature_inferior)

    new_alert.humidity_superior = int(humidity_superior)
    new_alert.humidity_inferior = int(humidity_inferior)

    new_alert.save()

    for email in recipients:
        try:
            existing_email = recipient.objects.get(email=email)
        except:
            new_email = recipient(
                email = email
            )
            new_email.save()
            existing_email = new_email
        new_alert.recipients.add(existing_email)        

    return JsonResponse({"message": 'Alerte créée'}, status=200, content_type='application/json')

@csrf_exempt
def update(request):
    if not request.method == "PUT":
        return error_response.bad_method()
    body = (request.body).decode()

    try:
        body = json.loads(body)
        id = body.get("id")
    except:
        return error_response.bad_request("Erreur de syntaxe des données transmises")
    
    try:
        recipients = body['recipients']
    except:
        return error_response.bad_request("Aucun destinataire")

    try:
        frequency = float(body.get('frequency'), None)
        temperature_superior = float(body.get('temperature_superior'), None)
        temperature_inferior = float(body.get('temperature_inferior'), None)
        humidity_superior = int(body.get('humidity_superior'), None)
        humidity_inferior = int(body.get('humidity_inferior'), None)
    except ValueError:
        return error_response.bad_request("Valeurs de température ou d'humidité ou frequency invalides")
    
    try:
        this_alert = alert.objects.get(id=id)
    except:
        return error_response.bad_request("Alerte introuvable")
    
    this_alert.frequency = int(frequency)
    
    this_alert.temperature_superior = float(temperature_superior)
    this_alert.temperature_inferior = float(temperature_inferior)

    this_alert.humidity_superior = int(humidity_superior)
    this_alert.humidity_inferior = int(humidity_inferior)
    this_alert.recipients = recipients

    this_alert.save()

    return JsonResponse({'message': 'Alerte mise à jour'}, content_type='application/json', status=200)

@csrf_exempt
def delete(request):
    if not request.method == "DELETE":
        return error_response.bad_method()
    id = request.GET.get('id')
    
    if not id:
        return error_response.bad_request("Aucun id fourni")
    
    try:
        this_alert = alert.objects.get(id=id)
    except:
        return error_response.bad_request("Alerte introuvable")
    
    try:
        this_alert.delete()
    except:
        return error_response.bad_request("Suppression de l'alerte impossible")

    return JsonResponse({'message': 'Alerte supprimée'}, content_type='application/json', status=200)
    