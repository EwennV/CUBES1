from django.urls import path, include
from . import views

urlpatterns = [
    path('list', views.list),
    path('create', views.create),
    path('update', views.update)
]