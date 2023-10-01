from django.db import models

class capteur(models.Model):
    id_capteur = models.AutoField(primary_key=True)
    name_capteur = models.CharField(max_length=64)
    position = models.CharField(max_length=64, null=True)

