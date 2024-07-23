from rest_framework import serializers

from .models import Planet
from .models import Terrain


class TerrainSerializer(serializers.ModelSerializer):

    class Meta:
        model = Terrain
        fields = ("id", "name")
        read_only_fields = ("id",)


class PlanetSerializer(serializers.ModelSerializer):
    terrains = TerrainSerializer(read_only=True, many=True)

    class Meta:
        model = Planet
        fields = ("id", "name", "population", "terrains")
        read_only_fields = ("id",)
