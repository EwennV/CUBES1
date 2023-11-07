from django.urls import path, include
from . import views
from .views import historique

urlpatterns = [
    path('home/', views.home),
    path('historique/', historique, name='historique')
]