from django_thread import Thread
import time
from datetime import datetime
from API import models
import requests
from API.scripts import traitement_donnees

from pathlib import Path
import os
import environ


# Script qui permet de récupérer les derniers relevés à partir de l'API des capteurs

# Pour récupérer les variables d'environnement, on doit d'abord aller chercher le ficher .env en passant par la racine du projet
# Le .parent permet de remonter dans les dossier à partir du dossier actuel
BASE_DIR = Path(__file__).resolve().parent.parent.parent
env = environ.Env()
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))


# Thread qui permet de d'éxécuter une suite d'instructions en boucle de manière asynchrone au projet global
class surveyCollect(Thread):
    def run(self):
        # Ce time.sleep permet d'attendre que le projet soit complétement initialisé pour ne pas avoir les potentiels print du thread au milieu de ceux de django
        time.sleep(1)
        while(True):
            
            # Récupération des données depuis l'API des capteurs, le paramètre account contient le token d'authentification permettant de se connecter à l'API
            try:
                response = requests.get(f'http://app.objco.com:8099/?account={env("API_KEY")}&limit=10')
                data = response.json()
                traitement_donnees.new(data)
            except:
                # Si nous n'avons pas de réponse de l'API ou que le format de retour n'est pas formatable en JSON, on print une erreur dans la console
                print("[API] [ERROR] Une erreur de communication avec l'API des capteurs est survenue")
            
            # On appelle la fonction traitement_donnees qui permet de traiter les nouvelles données reçues
            # Dans le cas où les capteurs font un relevé minimum toute les 5 minutes il est inutile de faire des requêtes toutes les secondes. On met donc un time.sleep de 5 minutes
            time.sleep(60*5) # Le time.sleep étant en secondes, on multiplie 60 secondes par 5 pour obtenir 5 minutes
            

# On lance le thread
thread = surveyCollect()
thread.start()