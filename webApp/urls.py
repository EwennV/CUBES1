from django.urls import path
from . import views


urlpatterns = [
    path('', views.dashboard, name='accueil'),
    path('historique/', views.historique, name='app_historique'),
    path('dashboard/', views.dashboard, name='app_dashboard'),
    path('alerte/', views.alerte, name='app_alerte'),
    path('carte/', views.carte, name='app_carte'),
    path('capteur/<int:sensorId>', views.capteur, name='app_capteur')
]
