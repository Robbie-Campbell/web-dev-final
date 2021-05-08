from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Category(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category', args=[self.id])
    
class Measurement(models.Model):
    unit_shorthand = models.CharField(max_length=10, default="g")
    unit_fullname = models.CharField(max_length=10, default="gram")

    def __str__(self):
        return self.unit_fullname

class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    weight = models.IntegerField()
    country_of_origin = models.CharField(max_length=100)
    unit_of_measurement = models.ForeignKey(Measurement, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Recipe(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="media/meals/", default="\core\media\media\meals\borat_mhFpThI.gif")
    description = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    ingredients = models.ManyToManyField(Ingredient)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    def get_absolute_url(self):
        return reverse('single', args=[self.id])

    def __str__(self):
        return self.title