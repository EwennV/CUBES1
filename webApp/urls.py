from django.urls import path, include
from . import views

urlpatterns = [
    path('dashboard/', views.home),
    path('historique/', views.historique, name='historique'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('alerte/', views.alerte, name='alerte'),
    path('carte/', views.carte, name='carte'),
    path('detail/', views.detail, name='detail')
]