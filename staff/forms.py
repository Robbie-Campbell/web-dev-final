from django.forms import ModelForm
from django import forms
from recipe.models import Recipe, Category
from ingredient.models import Measurement

class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = "__all__"

class MeasurementForm(ModelForm):
    class Meta:
        model = Measurement
        fields = "__all__"