from importlib import import_module

from django.conf import settings
from django.http import HttpRequest
from django.test import Client, SimpleTestCase, TestCase
from django.urls import reverse
from recipe.forms import CreateRecipeForm, EditRecipeForm

from recipe.models import Category, Recipe
from account.models import UserBase


class TestPayment(TestCase):

    def setUp(self):
        self.client = Client()
        user = UserBase.objects.create(username='admin', email='test@email.com', password='test')
        password = "testpass"
        admin = UserBase.objects.create_superuser("tester", "myemail@test.com", password)
        self.client.login(email=admin.email, password=password)