import pytest

from planets.models import Climate
from planets.models import Planet
from planets.models import Terrain


@pytest.mark.django_db
def test_planet_model():
    """
    Test case for the Planet model.

    This test creates a Planet object with a name and population,
    and then asserts that the attributes of the object are set correctly.
    """
    planet = Planet.objects.create(name="Earth", population=8_100_000_000)
    assert planet.name == "Earth"
    assert planet.population == 8_100_000_000
    assert str(planet) == planet.name


@pytest.mark.django_db
def test_planet_model_without_population():
    """
    Test case to verify the behavior of the Planet model when created without a population.
    """
    planet = Planet.objects.create(name="Mars")
    assert planet.name == "Mars"
    assert planet.population == None
    assert str(planet) == planet.name


@pytest.mark.django_db
def test_planet_model_with_two_terrains():
    """
    Test case to verify the behavior of the Planet model when it has two terrains.
    """
    planet = Planet.objects.create(name="Mars")
    terrain_one = Terrain.objects.create(name="desert")
    terrain_two = Terrain.objects.create(name="mountain")
    planet.terrains.add(terrain_one)
    planet.terrains.add(terrain_two)
    assert planet.name == "Mars"
    assert planet.population == None
    assert planet.terrains.count() == 2


@pytest.mark.django_db
def test_planet_model_with_two_climates():
    """
    Test case to verify the behavior of the Planet model when it has two climates.
    """
    planet = Planet.objects.create(name="Mars")
    climate_one = Climate.objects.create(name="arid")
    climate_two = Climate.objects.create(name="cold")
    planet.climates.add(climate_one)
    planet.climates.add(climate_two)
    assert planet.name == "Mars"
    assert planet.population == None
    assert planet.climates.count() == 2
