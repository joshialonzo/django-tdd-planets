from django.urls import path

from .views import PlanetList


urlpatterns = [
    path("api/planets/", PlanetList.as_view()),
]
