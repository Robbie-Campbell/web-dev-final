from django.forms import ModelForm
from recipe.models import Recipe
from .models import Ingredient
        
class Ingredient(ModelForm):
    class Meta:
        model = Ingredient
        fields = '__all__'
        exclude = ["recipe"]