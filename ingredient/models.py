from django.db import models
from recipe.models import Recipe


class Measurement(models.Model):
    unit_shorthand = models.CharField(max_length=10)
    unit_fullname = models.CharField(max_length=10)

    def __str__(self):
        return self.unit_fullname


class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    weight = models.IntegerField()
    country_of_origin = models.CharField(max_length=100)
    unit_of_measurement = models.ForeignKey(Measurement, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
