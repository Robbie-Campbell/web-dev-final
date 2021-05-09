from django.forms import ModelForm
from django import forms
from . models import Recipe, Category
from ingredient.models import Measurement

class CreateRecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = ["title", "description", "price", "category"]

class EditRecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = ["title", "image", "description", "price", "category"]