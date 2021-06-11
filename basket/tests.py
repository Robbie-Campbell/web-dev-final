from django.test import Client, TestCase
from django.urls import reverse

from recipe.models import Category, Recipe
from account.models import UserBase


class TestBasketView(TestCase):
    def setUp(self):
        self.client = Client()
        user = UserBase.objects.create(username='admin', email='test@email.com', password='test')
        password = "testpass"
        admin = UserBase.objects.create_superuser("tester", "myemail@test.com", password)
        Category.objects.create(title='test', description='test')
        Recipe.objects.create(category_id=1, title='pasta', author=user, price='20.00', image='default.jpg')
        Recipe.objects.create(category_id=1, title='beans', author=user, price='20.00', image='default.jpg')
        Recipe.objects.create(category_id=1, title='cheese', author=user, price='20.00', image='default.jpg')
        self.client.post(
            reverse('basket:basket_add'), {"recipeid": 1, "recipeqty": 1, "action": "post"}, xhr=True)
        self.client.post(
            reverse('basket:basket_add'), {"recipeid": 2, "recipeqty": 2, "action": "post"}, xhr=True)

    def test_basket_url(self):
        response = self.client.get(reverse('basket:basket_summary'))
        self.assertEqual(response.status_code, 200)

    def test_basket_add(self):
        response = self.client.post(
            reverse('basket:basket_add'), {"recipeid": 3, "recipeqty": 1, "action": "post"}, xhr=True)
        self.assertEqual(response.json(), {'qty': 4})
        response = self.client.post(
            reverse('basket:basket_add'), {"recipeid": 2, "recipeqty": 1, "action": "post"}, xhr=True)
        self.assertEqual(response.json(), {'qty': 3})

    def test_basket_delete(self):
        response = self.client.post(
            reverse('basket:basket_delete'), {"recipeid": 2, "action": "post"}, xhr=True)
        self.assertEqual(response.json(), {'qty': 1, 'subtotal': '20.00'})

    def test_basket_update(self):
        response = self.client.post(
            reverse('basket:basket_update'), {"recipeid": 2, "recipeqty": 1, "action": "post"}, xhr=True)
        self.assertEqual(response.json(), {'qty': 2, 'subtotal': '40.00'})