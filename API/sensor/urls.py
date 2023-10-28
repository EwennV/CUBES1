from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.sensor),
    path('create', views.create),
    path('update', views.update)
]