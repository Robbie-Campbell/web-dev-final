from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from recipe.models import Category, Recipe
from account.models import UserBase


class TestCategoriesModel(TestCase):

    def setUp(self):
        self.data1 = Category.objects.create(title='django')

    def test_category_model_entry(self):
        """
        Test Category model data insertion/types/field attributes
        """
        data = self.data1
        self.assertTrue(isinstance(data, Category))
        self.assertEqual(str(data), 'django')

    def test_category_url(self):
        """
        Test category model slug and URL reverse
        """
        data = self.data1
        response = self.client.post(
            reverse('recipe:category', args=[1]))
        self.assertEqual(response.status_code, 200)


class TestrecipesModel(TestCase):
    def setUp(self):
        Category.objects.create(title='django')
        author = UserBase.objects.create(username='admin', email='test@email.com', password='test')
        self.data1 = Recipe.objects.create(category_id=1, title='django beginners', author=author,
                                           price='20.00', image='django')

    def test_recipes_model_entry(self):
        """
        Test recipe model data insertion/types/field attributes
        """
        data = self.data1
        self.assertTrue(isinstance(data, Recipe))
        self.assertEqual(str(data), 'django beginners')

    def test_recipes_url(self):
        """
        Test recipe model slug and URL reverse
        """
        data = self.data1
        url = reverse('recipe:recipe_single', args=[1])
        self.assertEqual(url, '/recipe/1/')
        response = self.client.post(
            reverse('recipe:recipe_single', args=[1]))
        self.assertEqual(response.status_code, 200)