from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin

from .models import Planet, CustomUser


@admin.register(CustomUser)
class UserAdmin(DefaultUserAdmin):
    pass


@admin.register(Planet)
class PlanetAdmin(admin.ModelAdmin):
    fields = ("name", "population")
    list_display = ("name", "population")
