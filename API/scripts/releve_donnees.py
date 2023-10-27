from django_thread import Thread
import time
from datetime import datetime
from API import models
import requests

from pathlib import Path
import os
import environ


BASE_DIR = Path(__file__).resolve().parent.parent
env = environ.Env()
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

class ExampleThread(Thread):
    def run(self):
        while(True):
            time.sleep(1)
            response = requests.get(f'http://app.objco.com:8099/?account=${env("API_KEY")}&limit=6')
            btc = response.json()
            print(btc['bpi']['USD']['rate'])

thread = ExampleThread()
thread.start()