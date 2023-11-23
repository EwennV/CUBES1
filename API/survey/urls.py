from django.urls import path, include
from . import views

app_name = "api_survey"

urlpatterns = [
    path('list', views.list, name="api_survey_list"),
]