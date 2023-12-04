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
    sensor= models.ForeignKey(sensor, on_delete=models.CASCADE)

class recipient(models.Model):
    email = models.EmailField(unique=True)

class alert(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    frequency = models.IntegerField()
    humidity_inferior = models.IntegerField()
    humidity_superior = models.IntegerField()
    temperature_inferior = models.FloatField()
    temperature_superior = models.FloatField()
    recipients = models.ManyToManyField(recipient)

