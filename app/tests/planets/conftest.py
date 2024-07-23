import pytest

from planets.models import Climate
from planets.models import Planet
from planets.models import Terrain


@pytest.fixture(scope="function")
def add_planet():
    """
    Fixture that adds a planet to the database.

    Args:
        name (str): The name of the planet.
        population (int, optional): The population of the planet. Defaults to None.

    Returns:
        Planet: The created planet object.
    """
    def _add_planet(name, population=None):
        planet = Planet.objects.create(
            name=name,
            population=population,
        )
        return planet
    return _add_planet


@pytest.fixture(scope="function")
def add_terrain():
    """
    Fixture that adds a terrain object to the database.

    Args:
        name (str): The name of the terrain.

    Returns:
        Terrain: The created terrain object.
    """
    def _add_terrain(name):
        terrain = Terrain.objects.create(name=name)
        return terrain
    return _add_terrain


@pytest.fixture(scope="function")
def add_climate():
    """
    Fixture that adds a climate object to the database.

    Args:
        name (str): The name of the climate.

    Returns:
        Climate: The created climate object.
    """
    def _add_climate(name):
        climate = Climate.objects.create(name=name)
        return climate
    return _add_climate
