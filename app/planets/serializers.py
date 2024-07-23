from rest_framework import serializers

from .models import Climate
from .models import Planet
from .models import Terrain


class ClimateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Climate
        fields = ("id", "name")
        read_only_fields = ("id",)


class TerrainSerializer(serializers.ModelSerializer):

    class Meta:
        model = Terrain
        fields = ("id", "name")
        read_only_fields = ("id",)


class PlanetSerializer(serializers.ModelSerializer):
    terrains = TerrainSerializer(read_only=True, many=True)
    climates = ClimateSerializer(read_only=True, many=True)

    class Meta:
        model = Planet
        fields = ("id", "name", "population", "terrains", "climates")
        read_only_fields = ("id",)
