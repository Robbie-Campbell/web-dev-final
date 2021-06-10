from django.forms import ModelForm
from . models import Recipe


class CreateRecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = ["title", "description", "price", "category"]

    def __init__(self, *args, **kwargs):
        super(CreateRecipeForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


class EditRecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = ["title", "image", "description", "price", "category"]

    def __init__(self, *args, **kwargs):
        super(EditRecipeForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
