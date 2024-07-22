import pytest


from planets.models import Planet


@pytest.fixture(scope="function")
def add_planet():
    def _add_planet(name, population=None):
        planet = Planet.objects.create(
            name=name,
            population=population,
        )
        return planet
    return _add_planet
