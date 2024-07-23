import pytest


from planets.models import Planet
from planets.models import Terrain


@pytest.fixture(scope="function")
def add_planet():
    def _add_planet(name, population=None):
        planet = Planet.objects.create(
            name=name,
            population=population,
        )
        return planet
    return _add_planet


@pytest.fixture(scope="function")
def add_terrain():
    def _add_terrain(name):
        terrain = Terrain.objects.create(name=name)
        return terrain
    return _add_terrain
