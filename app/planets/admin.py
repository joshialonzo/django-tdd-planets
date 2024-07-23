from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin

from .models import CustomUser
from .models import Planet
from .models import Terrain


@admin.register(CustomUser)
class UserAdmin(DefaultUserAdmin):
    pass


@admin.register(Planet)
class PlanetAdmin(admin.ModelAdmin):
    fields = ("name", "population")
    list_display = ("name", "population", "get_terrains")

    @admin.display(description="terrains")
    def get_terrains(self, obj: Planet):
        return ", ".join([terrain.name for terrain in obj.terrains.all()])

@admin.register(Terrain)
class TerrainAdmin(admin.ModelAdmin):
    fields = ("name",)
    list_display = ("name",)
