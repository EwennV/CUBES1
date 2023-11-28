from django.http import JsonResponse
from django.http import HttpResponse
from API.models import alert, recipient
from django.core import serializers  
from API.scripts import error_response
import json
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def create(request):
    if not request.method == "POST":
        return error_response.bad_method()
    
    frequency = request.GET.get("frequency")
    temperature_superior = request.GET.get('temperature_superior') or None
    temperature_inferior = request.GET.get('temperature_inferior') or None
    humidity_superior = request.GET.get('humidity_superior') or None
    humidity_inferior = request.GET.get('humidity_inferior') or None
    body = (request.body).decode()

    try:
        body = json.loads(body)
    except:
        return error_response.bad_request("Erreur de syntaxe des données transmises")
    
    try:
        recipients = body['recipients']
    except:
        return error_response.bad_request("Aucun destinataire")

    if not frequency or not int(frequency):
        return error_response.bad_request("Fréquence invalide")

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

def list(request):
    if not request.method == "GET":
        return error_response.bad_method()
    
    id = request.GET.get('id')

    if id:
        if not alert.objects.get(id=id):
            return error_response.bad_request('Alerte introuvable')
        data = alert.objects.get(id=id)
    else:
        data = alert.objects.all()

    data_json = serializers.serialize('json', data)
    return HttpResponse(data_json, content_type="application/json", status=200)


@csrf_exempt
def update(request):
    if not request.method == "PUT":
        return error_response.bad_method()
    id = request.GET.get('id')
    
    if not id:
        return error_response.bad_request("Aucun id fourni")
    
    frequency = request.GET.get("frequency")
    temperature_superior = request.GET.get('temperature_superior') or None
    temperature_inferior = request.GET.get('temperature_inferior') or None
    humidity_superior = request.GET.get('humidity_superior') or None
    humidity_inferior = request.GET.get('humidity_inferior') or None
    body = (request.body).decode()

    if not frequency or not int(frequency):
        return error_response.bad_request("Fréquence invalide")

    # if 0 <= humidity_inferior <= 100

    try:
        body = json.loads(body)
    except:
        return error_response.bad_request("Erreur de syntaxe des données transmises")
    
    try:
        recipients = body['recipients']
    except:
        return error_response.bad_request("Aucun destinataire")
    
    try:
        this_alert = alert.objects.get(id=id)
    except:
        return error_response.bad_request("Alerte introuvable")
    
    this_alert.frequency = frequency
    
    this_alert.temperature_superior = int(temperature_superior)
    this_alert.temperature_inferior = int(temperature_inferior)

    this_alert.humidity_superior = int(humidity_superior)
    this_alert.humidity_inferior = int(humidity_inferior)

    this_alert.save()

    return JsonResponse({'message': 'Alerte mise à jour'}, content_type='application/json', status=200)

@csrf_exempt
def delete(request):
    if not request.method == "DELETE":
        return error_response.bad_method()
    id = request.GET.get('id')
    
    if not id:
        return error_response.bad_request("Aucun id fourni")
    