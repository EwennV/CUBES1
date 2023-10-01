from django.db import models

class capteurs(models.Model):
    id_capteur = models.AutoField(primary_key=True)
    nom_capteur = models.fields.CharField(max_length=100)