from django.shortcuts import render
from django.http import JsonResponse  

# Create your views here.

def list(request):
    data = {
        'name': 'John Doe',
        'age': 30,
        'email': 'john.doe@example.com'
    }
    return JsonResponse(data, status=200)
