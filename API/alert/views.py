from django.http import JsonResponse
from django.http import HttpResponse
from django.forms.models import model_to_dict
from django.core.serializers.json import DjangoJSONEncoder
from django.core.serializers import serialize
from API.models import alert, recipient
from API.scripts import error_response
import json
from django.views.decorators.csrf import csrf_exempt
import validators

def index(request):
    if not request.method == "GET":
        return error_response.bad_method()
    
    alertId = request.GET.get('id')

    alerts = []

    if alertId:
        if not alert.objects.filter(id=alertId):
            return error_response.bad_request('Alerte introuvable')
        data = alert.objects.filter(id=alertId)
    else:
        data = alert.objects.all()

    for alert_instance in data:
        alert_dict = model_to_dict(alert_instance)

        alert_dict['id'] = alert_instance.id
        alert_dict['recipients'] = [recipient.email for recipient in alert_instance.recipients.all()]
        alerts.append(alert_dict)

    return JsonResponse(alerts,safe=False , content_type="application/json", status=200)

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
        print(body)
    except:
        return error_response.bad_request("Erreur de syntaxe des données transmises")
    
    try:
        id = body['id']
    except:
        return error_response.bad_request("Id invalide")

    try:
        this_alert = alert.objects.get(id=id)
    except:
        return error_response.bad_request('Alerte inexistante')

    try:
        recipients = body['recipients']
        if not recipients : return error_response.bad_request('Aucun destinataire.')
        for email in recipients:
            if True != validators.email(email): return error_response.bad_request("Adresse mail des destinaires invalide")
    except:
        return error_response.bad_request("Aucun destinataire")

    try:
        frequency = int(body['frequency']) if body['frequency'] !="" else None
        if not frequency or frequency < 5:
            return error_response.bad_method("Fréquence invalide, doit être supérieur à 5 minutes")
        temperature_superior = float(body['temperature_superior']) if body['temperature_superior'] != "" else None
        temperature_inferior = float(body['temperature_inferior']) if body['temperature_inferior'] != "" else None
        humidity_superior = int(body['humidity_superior']) if body['humidity_superior'] != "" else None
        humidity_inferior = int(body['humidity_inferior']) if body['humidity_inferior'] != "" else None
    except ValueError:
        return error_response.bad_request("Valeurs de température ou d'humidité ou fréquence invalide")
    
    this_alert.frequency = frequency

    this_alert.temperature_superior = temperature_superior
    this_alert.temperature_inferior = temperature_inferior

    this_alert.humidity_superior = humidity_superior
    this_alert.humidity_inferior = humidity_inferior
    
    this_alert.recipients.clear()
    for email in recipients:
        try:
            existing_email = recipient.objects.get(email=email)
        except:
            new_email = recipient(
                email = email
            )
            new_email.save()
            existing_email = new_email
        this_alert.recipients.add(existing_email)      

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
    