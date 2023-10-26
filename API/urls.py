from django.urls import path, include

urlpatterns = [
    path('captor/', include('API.captor.urls')),
    path('survey/', include('API.survey.urls'))
]