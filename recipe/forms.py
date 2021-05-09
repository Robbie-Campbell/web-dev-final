from django.forms import ModelForm
from django import forms
from . models import Recipe, Ingredient

class PictureWidget(forms.widgets.Widget):
    def render(self, name, value, attrs=None, **kwargs):
        html =  Template("""<img src="$link"/>""")
        return mark_safe(html.substitute(link=value))

class CreateRecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = ["title", "description", "price", "category"]

class EditRecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = ["title", "image", "description", "price", "category"]
        
class AddIngredientForm(ModelForm):
    class Meta:
        model = Ingredient
        fields = '__all__'
        exclude = ["recipe"]