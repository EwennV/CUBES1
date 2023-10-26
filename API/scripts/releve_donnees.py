from django_thread import Thread
import time
from API import models

class ExampleThread(Thread):
    def run(self):
        time.sleep(1)
        data = models.captor.objects.all()

        for captor in data:
            print(captor)

thread = ExampleThread()
thread.start()