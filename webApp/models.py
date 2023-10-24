import uuid
from django.db import models

class capteur(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name_capteur = models.CharField(max_length=64)
    lattitudde = models.FloatField(null=True)
    longitude = models.FloatField(null=True)

    def __str__(self) -> str:
        return id

class survey(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    temperature = models.FloatField(null=True)
    humidity = models.IntegerField(null=True)
    battery_level = models.FloatField()
    rssi = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    capteur = models.ForeignKey(capteur, null=True, on_delete=models.SET_NULL)