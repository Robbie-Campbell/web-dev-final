from importlib import import_module

from django.conf import settings
from django.http import HttpRequest
from django.test import Client, SimpleTestCase, TestCase
from django.urls import reverse
from recipe.forms import CreateRecipeForm, EditRecipeForm

from recipe.models import Category, Recipe
from account.models import UserBase


class TestRecipeViews(TestCase):
    def setUp(self):
        self.client = Client()
        user = UserBase.objects.create(username='admin', email='test@email.com', password='test')
        password = "testpass"
        admin = UserBase.objects.create_superuser("tester", "myemail@test.com", password)
        self.client.login(email=admin.email, password=password)
        self.category = Category.objects.create(title='django')
        self.recipe = Recipe.objects.create(id=1, category=self.category, title='django beginners', description="lorem", author=user, published=False, price='20.00', image='default.png', method="lorem")

    def test_url_allowed_hosts(self):
        response = self.client.get('/', HTTP_HOST='test.com')
        self.assertEqual(response.status_code, 400)
        response = self.client.get('/', HTTP_HOST='yourdomain.com')
        self.assertEqual(response.status_code, 200)

    def test_homepage_url(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_recipe_list_url(self):
        response = self.client.get(reverse('recipe:recipe_list'))
        self.assertEqual(response.status_code, 200)

    def test_recipe_category_list_url(self):
        response = self.client.get(reverse('recipe:category', args=[1]))
        self.assertEqual(response.status_code, 200)

    def test_recipe_detail_url(self):
        response = self.client.get(reverse('recipe:recipe_single', args=[1]))
        self.assertEqual(response.status_code, 200)

    def test_recipe_create_get(self):
        response = self.client.get(reverse('recipe:create_recipe'))
        self.assertEqual(response.status_code, 200)

    def test_recipe_create_form(self):
        form = CreateRecipeForm(data={"title": self.recipe.title, "description": self.recipe.description, "price": self.recipe.price, "category": self.recipe.category})
        self.assertTrue(form.is_valid())

    def test_recipe_create_post(self):
        response = self.client.post(reverse('recipe:create_recipe'), data=self.recipe.__dict__)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Recipe.objects.first().id, 1)

    def test_recipe_edit_form(self):
        form = CreateRecipeForm(data={"title": self.recipe.title, "image":self.recipe.image, "description": self.recipe.description, "price": self.recipe.price, "category": self.recipe.category})
        self.assertTrue(form.is_valid())

    def test_recipe_edit_get(self):
        self.client.post(reverse('recipe:create_recipe'), data=self.recipe.__dict__)
        response = self.client.get(reverse('recipe:edit_recipe', args=[self.recipe.id]))
        self.assertEqual(response.status_code, 200)
    
    def test_recipe_delete(self):
        self.client.post(reverse('recipe:create_recipe'), data=self.recipe.__dict__)
        response = self.client.post(reverse('recipe:delete_recipe', args=[self.recipe.id]))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Recipe.objects.count(), 0)