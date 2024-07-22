import json

import pytest

from planets.models import Planet


@pytest.mark.django_db
def test_add_planet(client):
    planets = Planet.objects.all()
    assert len(planets) == 0

    resp = client.post(
        "/api/planets/",
        {
            "name": "Earth",
            "population": 8_100_000_000,
        },
        content_type="application/json"
    )
    assert resp.status_code == 201
    assert resp.data["name"] == "Earth"
    assert resp.data["population"] == 8_100_000_000

    planets = Planet.objects.all()
    assert len(planets) == 1


@pytest.mark.django_db
def test_add_planet_invalid_json(client):
    planets = Planet.objects.all()
    assert len(planets) == 0

    resp = client.post(
        "/api/planets/",
        {},
        content_type="application/json"
    )
    assert resp.status_code == 400

    planets = Planet.objects.all()
    assert len(planets) == 0


@pytest.mark.django_db
def test_add_planet_invalid_json_keys(client):
    planets = Planet.objects.all()
    assert len(planets) == 0

    resp = client.post(
        "/api/planets/",
        {
            "population": 100,
        },
        content_type="application/json"
    )
    assert resp.status_code == 400

    planets = Planet.objects.all()
    assert len(planets) == 0


@pytest.mark.django_db
def test_get_single_planet(client):
    planet = Planet.objects.create(name="Earth", population=8_100_000_000)
    resp = client.get(f"/api/planets/{planet.id}/")
    assert resp.status_code == 200
    assert resp.data["name"] == "Earth"


def test_get_single_planet_incorrect_id(client):
    resp = client.get(f"/api/planets/foo/")
    assert resp.status_code == 404
