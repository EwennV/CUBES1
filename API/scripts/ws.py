from django_thread import Thread
import time
from API import models

class ExampleThread(Thread):
    def run(self):
        time.sleep(1)
        print(models.captor.objects.all())

thread = ExampleThread()
thread.start()