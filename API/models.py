from django.db import models

class captor(models.Model):
    name = models.CharField(max_length=64)
    lattitude = models.FloatField()
    longitude = models.FloatField()

class survey(models.Model):
    temperature = models.FloatField()
    humidity = models.IntegerField()
    battery_level = models.FloatField()
    rssi = models.IntegerField(max_length=3)
    date = models.DateField()
    capteur_id = models.IntegerField(max_length=15)

class alert(models.Model):
    frequency = models.IntegerField(max_length=6)
    type = models.CharField(max_length=45)
    limit = models.CharField(max_length=45)

class type(models.Model):
    name = models.CharField(max_length=45)

class recipient(models.Model):
    email = models.CharField(max_length=255)

class alert_has_recipient(models.Model):    
    alert_date = models.IntegerField()
    recipient_email = models.CharField(max_length=255)