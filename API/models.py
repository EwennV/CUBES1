from django.db import models
import uuid

class captor(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=64)
    lattitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)

class survey(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    temperature = models.FloatField()
    humidity = models.IntegerField()
    battery_level = models.FloatField()
    rssi = models.IntegerField()
    date = models.DateField()
    capteur_id = models.IntegerField()

class recipient(models.Model):
    email = models.CharField(max_length=255)

class alert(models.Model):
    id_alert = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    frequency = models.IntegerField()
    type = models.CharField(max_length=45)
    limit = models.CharField(max_length=45)
    recipients = models.ManyToManyField(recipient)

