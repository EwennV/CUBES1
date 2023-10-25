from django.urls import path, include
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('captor/', include('API.captor.urls'))
]