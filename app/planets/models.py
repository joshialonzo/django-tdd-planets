from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    """
    A custom user model that extends the AbstractUser class.

    This model represents a user in the application and inherits all the fields and methods
    from the AbstractUser class provided by Django's authentication system.

    Additional customizations can be made to this model as per the application's requirements.
    """
    pass


class Planet(models.Model):
    """
    Represents a planet in the solar system.
    """

    name = models.CharField(max_length=255)
    population = models.BigIntegerField(null=True)
    terrains = models.ManyToManyField("Terrain", related_name="planets")
    climates = models.ManyToManyField("Climate", related_name="planets")

    def __str__(self):
        return self.name


class Terrain(models.Model):
    """
    Represents a type of terrain on a planet.
    """

    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Climate(models.Model):
    """
    Represents a climate type.
    """

    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
