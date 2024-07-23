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
def test_get_single_planet(client, add_planet):
    planet = add_planet(name="Earth", population=8_100_000_000)
    resp = client.get(f"/api/planets/{planet.id}/")
    assert resp.status_code == 200
    assert resp.data["name"] == "Earth"


def test_get_single_planet_incorrect_id(client):
    resp = client.get(f"/api/planets/foo/")
    assert resp.status_code == 404


@pytest.mark.django_db
def test_get_all_planets(client, add_planet):
    planet_one = add_planet(name="Earth", population=1_000_000)
    planet_two = add_planet(name="Mars")
    resp = client.get(f"/api/planets/")
    assert resp.status_code == 200
    assert resp.data[0]["name"] == planet_one.name
    assert resp.data[1]["name"] == planet_two.name


@pytest.mark.django_db
def test_remove_planet(client, add_planet):
    planet = add_planet(name="Earth", population=8_100_000_000)

    resp = client.get(f"/api/planets/{planet.id}/")
    assert resp.status_code == 200
    assert resp.data["name"] == "Earth"

    resp_two = client.delete(f"/api/planets/{planet.id}/")
    assert resp_two.status_code == 204

    resp_three = client.get("/api/planets/")
    assert resp_three.status_code == 200
    assert len(resp_three.data) == 0


@pytest.mark.django_db
def test_remove_planet_incorrect_id(client):
    resp = client.delete(f"/api/planets/99/")
    assert resp.status_code == 404


@pytest.mark.django_db
def test_update_planet(client, add_planet):
    planet = add_planet(name="Earth", population=8_100_000_000)

    resp = client.put(
        f"/api/planets/{planet.id}/",
        {"name": "Earth", "population": 8_300_000_000},
        content_type="application/json"
    )
    assert resp.status_code == 200
    assert resp.data["name"] == "Earth"
    assert resp.data["population"] == 8_300_000_000

    resp_two = client.get(f"/api/planets/{planet.id}/")
    assert resp_two.status_code == 200
    assert resp_two.data["name"] == "Earth"
    assert resp.data["population"] == 8_300_000_000


@pytest.mark.django_db
def test_update_planet_incorrect_id(client):
    resp = client.put(f"/api/planets/99/")
    assert resp.status_code == 404


@pytest.mark.django_db
def test_update_planet_invalid_json(client, add_planet):
    planet = add_planet(name="Earth", population=8_100_000_000)
    resp = client.put(f"/api/planets/{planet.id}/", {}, content_type="application/json")
    assert resp.status_code == 400


@pytest.mark.django_db
def test_update_planet_invalid_json_keys(client, add_planet):
    planet = add_planet(name="Earth", population=8_100_000_000)

    resp = client.put(
        f"/api/planets/{planet.id}/",
        {"title": "The Big Lebowski", "genre": "comedy"},
        content_type="application/json",
    )
    assert resp.status_code == 400


@pytest.mark.django_db
def test_add_planet_with_terrains(client, add_planet, add_terrain):
    planet = add_planet(name="Earth", population=8_100_000_000)
    terrain_one = add_terrain(name="desert")
    terrain_two = add_terrain(name="mountain")
    planet.terrains.add(terrain_one)
    planet.terrains.add(terrain_two)

    resp = client.get(
        f"/api/planets/{planet.id}/",
        content_type="application/json"
    )
    assert resp.status_code == 200
    assert resp.data["name"] == "Earth"
    assert resp.data["population"] == 8_100_000_000
    assert len(resp.data["terrains"]) == 2
    assert resp.data["terrains"][0]["name"] == "desert"
    assert resp.data["terrains"][1]["name"] == "mountain"


@pytest.mark.django_db
def test_add_planet_with_climates(client, add_planet, add_climate):
    planet = add_planet(name="Earth", population=8_100_000_000)
    terrain = add_climate(name="temperate")
    planet.climates.add(terrain)

    resp = client.get(
        f"/api/planets/{planet.id}/",
        content_type="application/json"
    )
    assert resp.status_code == 200
    assert resp.data["name"] == "Earth"
    assert resp.data["population"] == 8_100_000_000
    assert len(resp.data["climates"]) == 1
    assert resp.data["climates"][0]["name"] == "temperate"
