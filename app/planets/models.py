from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    pass


class Planet(models.Model):
    name = models.CharField(max_length=255)
    population = models.BigIntegerField()

    def __str__(self):
        return self.name
