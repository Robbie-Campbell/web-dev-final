from importlib import import_module

from django.conf import settings
from django.http import HttpRequest
from django.test import Client, SimpleTestCase, TestCase
from django.urls import reverse

from ingredient.forms import IngredientForm

from ingredient.models import Ingredient, Measurement
from account.models import UserBase
from recipe.models import Category, Recipe


class TestIngredients(TestCase):

    def setUp(self):
        self.client = Client()
        user = UserBase.objects.create(username='admin', email='test@email.com', password='test')
        password = 'testpass'
        admin = UserBase.objects.create_superuser('tester', 'myemail@test.com', password)
        self.client.login(email=admin.email, password=password)
        self.category = Category.objects.create(title='django')
        self.recipe = Recipe.objects.create(id=1, category=self.category, title='django beginners', description='lorem', author=user, published=False, price='20.00', image='default.png', method='lorem')
        self.measurement = Measurement.objects.create(id=1, unit_shorthand='test', unit_fullname='tester')
        self.ingredient = Ingredient.objects.create(id=1, name='test', weight=200, country_of_origin='spain', unit_of_measurement=self.measurement, recipe=self.recipe)
    
    def test_ingredient_create_post(self):
        response = self.client.post(reverse('ingredient:create_ingredient', args=[self.recipe.id]), data=self.ingredient.__dict__)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Ingredient.objects.first().id, 1)

    def test_ingredient_create_form(self):
        form = IngredientForm(data={'name':'test', 'weight':200, 'country_of_origin':'spain', 'unit_of_measurement':self.measurement})
        self.assertTrue(form.is_valid())

    def test_ingredient_create_get(self):
        response = self.client.get(reverse('ingredient:create_ingredient', args=[self.recipe.id]))
        self.assertEqual(response.status_code, 200)
    
    def test_ingredient_delete(self):
        response = self.client.post(reverse('ingredient:delete_ingredient', args=[self.ingredient.id]))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Ingredient.objects.count(), 0)