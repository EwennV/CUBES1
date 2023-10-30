from django.db import models
import uuid

class sensor(models.Model):
    id = models.CharField(primary_key=True, max_length=8)
    name = models.CharField(max_length=64)
    lattitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)

class survey(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    idSurvey = models.IntegerField()
    temperature = models.FloatField(null=True)
    humidity = models.IntegerField(null=True)
    battery_level = models.IntegerField()
    rssi = models.IntegerField()
    date = models.DateTimeField()
    sensor_id = models.CharField(max_length=8)

class recipient(models.Model):
    email = models.CharField(max_length=255)

class alert(models.Model):
    id_alert = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    frequency = models.IntegerField()
    type = models.CharField(max_length=45)
    limit = models.CharField(max_length=45)
    recipients = models.ManyToManyField(recipient)

