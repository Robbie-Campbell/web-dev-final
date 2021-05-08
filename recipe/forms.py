from django.forms import ModelForm
from django import forms
from . models import Recipe, Ingredient


class AddRecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = ["title", "description", "price", "category"]
        
class AddIngredientForm(ModelForm):
    class Meta:
        model = Ingredient
        fields = '__all__'