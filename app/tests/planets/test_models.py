import pytest

from planets.models import Planet


@pytest.mark.django_db
def test_planet_model():
    planet = Planet.objects.create(name="Earth", population=8_100_000_000)
    assert planet.name == "Earth"
    assert planet.population == 8_100_000_000
    assert str(planet) == planet.name


@pytest.mark.django_db
def test_planet_model_without_population():
    planet = Planet.objects.create(name="Mars")
    assert planet.name == "Mars"
    assert planet.population == None
    assert str(planet) == planet.name