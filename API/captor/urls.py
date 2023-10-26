from django.urls import path, include
from . import views

urlpatterns = [
    path('list', views.captor_list),
    path('create', views.create),
    path('update', views.update)
]