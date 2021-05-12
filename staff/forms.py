from django.forms import ModelForm
from django import forms
from recipe.models import Recipe, Category
from ingredient.models import Measurement

class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(CategoryForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

class MeasurementForm(ModelForm):
    class Meta:
        model = Measurement
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(MeasurementForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'