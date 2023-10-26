from django.db import models

class captor(models.Model):
    name = models.CharField(max_length=64)
    lattitude = models.FloatField()
    longitude = models.FloatField()

class survey(models.Model):
    temperature = models.FloatField()
    humidity = models.Int
    battery_level = models.FloatField()
    rssi = models.
