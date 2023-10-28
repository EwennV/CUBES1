from django_thread import Thread
import time
from datetime import datetime
from API import models
import requests
from API.scripts import traitement_donnees

from pathlib import Path
import os
import environ


BASE_DIR = Path(__file__).resolve().parent.parent
env = environ.Env()
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

class ExampleThread(Thread):
    def run(self):
        time.sleep(1)
        while(True):
            response = requests.get(f'http://app.objco.com:8099/?account=GX1GLQRVNM&limit=10')
            data = response.json()
            traitement_donnees.new(data)
            time.sleep(40)
            

thread = ExampleThread()
thread.start()