from django.urls import path

from .views import PlanetDetail
from .views import PlanetList


urlpatterns = [
    path("api/planets/", PlanetList.as_view()),
    path("api/planets/<int:pk>/", PlanetDetail.as_view()),
]
