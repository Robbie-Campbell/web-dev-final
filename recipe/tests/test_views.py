from importlib import import_module

from django.conf import settings
from django.http import HttpRequest
from django.test import Client, TestCase
from django.urls import reverse

from recipe.models import Category, Recipe
from account.models import UserBase


class TestViewResponses(TestCase):
    def setUp(self):
        self.c = Client()
        user = UserBase.objects.create(username='admin', email='test@email.com', password='test')
        Category.objects.create(title='django')
        Recipe.objects.create(category_id=1, title='django beginners', author=user, price='20.00', image='django')

    def test_url_allowed_hosts(self):
        response = self.c.get('/', HTTP_HOST='test.com')
        self.assertEqual(response.status_code, 400)
        response = self.c.get('/', HTTP_HOST='yourdomain.com')
        self.assertEqual(response.status_code, 200)

    def test_homepage_url(self):
        response = self.c.get('/')
        self.assertEqual(response.status_code, 200)

    def test_recipe_category_list_url(self):
        response = self.c.get(
            reverse('recipe:recipe_list'))
        self.assertEqual(response.status_code, 200)

    def test_recipe_list_url(self):
        response = self.c.get(
            reverse('recipe:category', args=[1]))
        self.assertEqual(response.status_code, 200)

    def test_recipe_detail_url(self):
        response = self.c.get(
            reverse('recipe:recipe_single', args=[1]))
        self.assertEqual(response.status_code, 200)