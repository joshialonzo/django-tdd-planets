from planets.serializers import ClimateSerializer
from planets.serializers import PlanetSerializer
from planets.serializers import TerrainSerializer


def test_valid_planet_serializer():
    valid_serializer_data = {
        "name": "Earth",
        "population": 8_100_000_000,
    }
    serializer = PlanetSerializer(data=valid_serializer_data)
    assert serializer.is_valid()
    assert serializer.validated_data == valid_serializer_data
    assert serializer.data == valid_serializer_data
    assert serializer.errors == {}


def test_invalid_planet_serializer():
    invalid_serializer_data = {
        "population": 1000000,
    }
    serializer = PlanetSerializer(data=invalid_serializer_data)
    assert not serializer.is_valid()
    assert serializer.validated_data == {}
    assert serializer.data == invalid_serializer_data
    assert serializer.errors == {"name": ["This field is required."]}


def test_valid_terrain_serializer():
    valid_serializer_data = {
        "name": "desert",
    }
    serializer = TerrainSerializer(data=valid_serializer_data)
    assert serializer.is_valid()
    assert serializer.validated_data == valid_serializer_data
    assert serializer.data == valid_serializer_data
    assert serializer.errors == {}


def test_invalid_terrain_serializer():
    invalid_serializer_data = {}
    serializer = TerrainSerializer(data=invalid_serializer_data)
    assert not serializer.is_valid()
    assert serializer.validated_data == {}
    assert serializer.data == invalid_serializer_data
    assert serializer.errors == {"name": ["This field is required."]}


def test_valid_climate_serializer():
    valid_serializer_data = {
        "name": "temperate",
    }
    serializer = ClimateSerializer(data=valid_serializer_data)
    assert serializer.is_valid()
    assert serializer.validated_data == valid_serializer_data
    assert serializer.data == valid_serializer_data
    assert serializer.errors == {}


def test_invalid_terrain_serializer():
    invalid_serializer_data = {}
    serializer = ClimateSerializer(data=invalid_serializer_data)
    assert not serializer.is_valid()
    assert serializer.validated_data == {}
    assert serializer.data == invalid_serializer_data
    assert serializer.errors == {"name": ["This field is required."]}
