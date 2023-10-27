from django_thread import Thread
import time
from datetime import datetime
from API import models
import requests

class ExampleThread(Thread):
    def run(self):
        while(True):
            time.sleep(1)
            response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
            btc = response.json()
            print(btc['bpi']['EUR']['rate'])

thread = ExampleThread()
thread.start()