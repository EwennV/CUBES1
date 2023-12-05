"""
WSGI config for cube1 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from API.scripts.releve_donnees import surveyCollect 

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cube1.settings')

application = get_wsgi_application()

thread = surveyCollect()
thread.start()