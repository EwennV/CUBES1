from django.urls import path, include
from . import views
from .views import historique
from .views import dashboard
from .views import alerte
from .views import carte
from .views import detail

urlpatterns = [
    path('home/', views.home),
    path('historique/', historique, name='historique'),
    path('dashboard/', dashboard, name='dashboard'),
    path('alerte/', alerte, name='alerte'),
    path('carte/', carte, name='carte'),
    path('detail/', detail, name='detail')
]