from django.db import models
from django.conf import settings
from django.urls import reverse

class Category(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category', args=[self.id])

class Recipe(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="meals/", default="borat.gif")
    description = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    published = models.BooleanField(default=False)

    def image_tag(self):
        return u'<img src="%s" />' % self.image.url
    
    def get_absolute_url(self):
        return reverse('single', args=[self.id])

    def __str__(self):
        return self.title