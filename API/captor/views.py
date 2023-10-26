from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers  
from API.models import captor
import json

# Create your views here.

def captor_list(request):
    data = serializers.serialize('json', captor.objects.all())
    return JsonResponse(data, content_type='application/json', status=200)

def create(request):
    data = {
        'name': 'John Doe',
        'age': 30,
        'email': 'john.doe@example.com'
    }
    return JsonResponse(data, status=200)

def update(request):
    data = {
        'name': 'John Doe',
        'age': 30,
        'email': 'john.doe@example.com'
    }
    return JsonResponse(data, status=200)