from planets.serializers import PlanetSerializer


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
