from rest_framework import serializers

from .models import Climate
from .models import Planet
from .models import Terrain


class ClimateSerializer(serializers.ModelSerializer):
    """
    Serializer for the Climate model.

    This serializer is used to convert Climate model instances into JSON
    representations and vice versa. It specifies the fields that should be
    included in the serialized output and any read-only fields.

    Attributes:
        model (Model): The Climate model class.
        fields (tuple): The fields to include in the serialized output.
        read_only_fields (tuple): The fields that should be read-only.

    """

    class Meta:
        model = Climate
        fields = ("id", "name")
        read_only_fields = ("id",)


class TerrainSerializer(serializers.ModelSerializer):
    """
    Serializer for the Terrain model.

    Serializes the Terrain model fields into JSON format.
    """

    class Meta:
        model = Terrain
        fields = ("id", "name")
        read_only_fields = ("id",)


class PlanetSerializer(serializers.ModelSerializer):
    """
    Serializer class for the Planet model.

    Serializes the Planet model fields and related terrains and climates.

    Attributes:
        terrains (TerrainSerializer): Serializer for the related terrains.
        climates (ClimateSerializer): Serializer for the related climates.

    Meta:
        model (Planet): The model class to be serialized.
        fields (tuple): The fields to be included in the serialized output.
        read_only_fields (tuple): The fields that are read-only and cannot be modified.
    """
    terrains = TerrainSerializer(read_only=True, many=True)
    climates = ClimateSerializer(read_only=True, many=True)

    class Meta:
        model = Planet
        fields = ("id", "name", "population", "terrains", "climates")
        read_only_fields = ("id",)
