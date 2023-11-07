from django.urls import path, include

urlpatterns = [
    path('sensor/', include('API.sensor.urls')),
    path('survey/', include('API.survey.urls'))
]