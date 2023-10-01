from django.shortcuts import render
from django.http import HttpResponse
from home.models import capteurs
def home(request):
    listCapteurs = capteurs.objects.all()
    return render(request, "home/home.html", {"capteurs":listCapteurs})

