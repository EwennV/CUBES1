from django.urls import path, include
from . import views

app_name = "api_sensor"

urlpatterns = [
    path('', views.sensor, name="api_sensor_list"),
    path('create', views.create, name="api_sensor_create"),
    path('update', views.update, name="api_sensor_update"),
    path('delete', views.delete, name="api_sensor_delete")
]