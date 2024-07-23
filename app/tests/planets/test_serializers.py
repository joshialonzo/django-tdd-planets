from planets.serializers import ClimateSerializer
from planets.serializers import PlanetSerializer
from planets.serializers import TerrainSerializer


def test_valid_planet_serializer():
    """
    Test case to verify the behavior of the PlanetSerializer when valid data is provided.
    """
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
    """
    Test case to verify the behavior of the PlanetSerializer when invalid data is provided.
    """
    invalid_serializer_data = {
        "population": 1000000,
    }
    serializer = PlanetSerializer(data=invalid_serializer_data)
    assert not serializer.is_valid()
    assert serializer.validated_data == {}
    assert serializer.data == invalid_serializer_data
    assert serializer.errors == {"name": ["This field is required."]}


def test_valid_terrain_serializer():
    """
    Test case to verify the behavior of the TerrainSerializer when provided with valid data.
    """
    valid_serializer_data = {
        "name": "desert",
    }
    serializer = TerrainSerializer(data=valid_serializer_data)
    assert serializer.is_valid()
    assert serializer.validated_data == valid_serializer_data
    assert serializer.data == valid_serializer_data
    assert serializer.errors == {}


def test_invalid_terrain_serializer():
    """
    Test case to verify the behavior of the TerrainSerializer when invalid data is provided.

    The test checks the following assertions:
    - The serializer should not be valid.
    - The validated data should be an empty dictionary.
    - The serialized data should be equal to the invalid data provided.
    - The errors dictionary should contain an error message for the "name" field.
    """
    invalid_serializer_data = {}
    serializer = TerrainSerializer(data=invalid_serializer_data)
    assert not serializer.is_valid()
    assert serializer.validated_data == {}
    assert serializer.data == invalid_serializer_data
    assert serializer.errors == {"name": ["This field is required."]}


def test_valid_climate_serializer():
    """
    Test case to verify the behavior of the ClimateSerializer when provided with valid data.

    It checks that the serializer is valid, the validated data matches the input data,
    the serialized data matches the input data, and there are no errors.

    """
    valid_serializer_data = {
        "name": "temperate",
    }
    serializer = ClimateSerializer(data=valid_serializer_data)
    assert serializer.is_valid()
    assert serializer.validated_data == valid_serializer_data
    assert serializer.data == valid_serializer_data
    assert serializer.errors == {}


def test_invalid_terrain_serializer():
    """
    Test case to verify the behavior of the ClimateSerializer when invalid data is provided.

    The test checks the following assertions:
    - The serializer should not be valid.
    - The validated data should be an empty dictionary.
    - The serialized data should be equal to the invalid data provided.
    - The errors should contain a specific error message for the 'name' field.
    """
    invalid_serializer_data = {}
    serializer = ClimateSerializer(data=invalid_serializer_data)
    assert not serializer.is_valid()
    assert serializer.validated_data == {}
    assert serializer.data == invalid_serializer_data
    assert serializer.errors == {"name": ["This field is required."]}
