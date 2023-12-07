from API import models
from datetime import datetime, timedelta
from django.utils import timezone
from django.core import serializers
from API.scripts.comparaison_alerte import compareAlert

sensors = models.sensor.objects.values('id')
list_sensors = list(sensors)


def new(data):

    list_alert = list(models.alert.objects.all())
    for survey in data:
        idThisSurvey = survey[0]
        if models.survey.objects.filter(idSurvey=idThisSurvey):
            return

        trame = survey[1]
        surveyDate = survey[2]
        formattedDate = datetime.strptime(surveyDate, "%a, %d %b %Y %H:%M:%S %Z")
        formattedDate = timezone.make_aware(formattedDate, timezone=timezone.utc)

        for sensor in list_sensors:
            if sensor['id'] in trame:
                position = trame.find(sensor['id'])
                sensorStatus = int(trame[position+8:position+10], 16)
                sensorBattery_voltage = float(int(trame[position+10:position+14], 16))
                sensorTemperature = float(int(trame[position+16:position+18], 16)/10)
                if int(trame[position+14:position+16], 16) == 40: sensorTemperature = -abs(sensorTemperature)
                sensorHumidity = float(int(trame[position+18:position+20], 16))
                if sensorHumidity == 255: sensorHumidity = None
                sensorRssi = int(trame[position+20:position+22], 16)
                newSurvey = models.survey(
                    idSurvey=idThisSurvey,
                    temperature=sensorTemperature,
                    humidity=sensorHumidity,
                    battery_level=sensorBattery_voltage,
                    rssi=sensorRssi,
                    date=formattedDate,
                    sensor_id=sensor['id'])
                # newSurvey.save() ################### A DECOMMENTER ###################
                print("[API] [NEW] : Nouveau relevé n°"+str(idThisSurvey))
                
                compareAlert(sensorTemperature, sensorHumidity, sensor)