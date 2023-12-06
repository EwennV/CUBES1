from django.urls import path, include
from . import views

app_name = "api_alert"

urlpatterns = [
    path('', views.index, name="api_alert_list"),
    path('create', views.create, name="api_alert_create"),
    path('update', views.update, name="api_alert_update"),
    path('delete', views.delete, name="api_alert_delete")
]