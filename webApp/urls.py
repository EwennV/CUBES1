from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('historique/', views.historique, name='historique'),
    path('alerte/', views.alerte, name='alerte'),
    path('carte/', views.carte, name='carte'),
    path('detail/<str:sensorId>', views.detail, name='detail'),
    path('modification/<str:sensorId>', views.modification, name='modification'),
    path('ajout/', views.ajout, name='ajout'),
]