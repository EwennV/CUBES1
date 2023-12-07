from API import models
from datetime import datetime, timedelta

alertSended = []

def compareAlert(sensorTemperature, sensorHumidity, sensor):
    list_alert = list(models.alert.objects.all())
    for alert in list_alert:
        try:
            alertType = None
            if sensorTemperature <= alert.temperature_inferior : alertType = "Température inférieure"
            if sensorTemperature >= alert.temperature_superior : alertType = "Température supérieure"
            if alert.humidity_inferior != None and sensorHumidity != None and sensorHumidity <= alert.humidity_inferior : alertType = "Humidité inférieure"
            if alert.humidity_inferior != None and sensorHumidity != None and sensorHumidity >= alert.humidity_superior : alertType = "Humidité supérieure"

            if alertType :
                if sensor["id"] not in alertSended:
                    try:
                        alertSended.append({
                            sensor["id"]: {
                                "expireAt": (datetime.now() + timedelta(minutes=alert.frequency)).timestamp(),
                            }
                        })
                        for recipient in alert.recipients.all():
                            print("[API] [EMAIL SENT] :", recipient.email)
                            
                        #########################################
                        # TODO ICI la fonction d'envoie de mail #
                        #########################################

                    except Exception as e:
                        print("Error")
                        print(e)
        except Exception as e:
            print(e) 
            print("[API] [ERROR] Une erreur est survenue lors de la gestion des alertes")


def updateSendedAlert():
    for alert in alertSended:
        if alert['expireAt'] > datetime.now().timestamp():
            alertSended.remove(alert)