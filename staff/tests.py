from django.test import Client, TestCase
from django.urls import reverse
from .forms import CategoryForm, MeasurementForm

from recipe.models import Category
from ingredient.models import Measurement
from account.models import UserBase


class TestStaff(TestCase):
    def setUp(self):
        self.client = Client()
        password = "testpass"
        admin = UserBase.objects.create_superuser("tester", "myemail@test.com", password)
        self.client.login(email=admin.email, password=password)
        self.category = Category.objects.create(id=1, title='django', description="lorem")
        self.measurement = Measurement.objects.create(id=1, unit_shorthand="test", unit_fullname="tester")

    def test_edit_list_url(self):
        response = self.client.get(reverse('staff:edit_cat_measurement'))
        self.assertEqual(response.status_code, 200)

    def test_category_create_get(self):
        response = self.client.get(reverse('staff:create_category'))
        self.assertEqual(response.status_code, 200)

    def test_category_create_form(self):
        form = CategoryForm(data={'title': self.category.title, 'description': self.category.description})
        self.assertTrue(form.is_valid())

    def test_category_create_post(self):
        response = self.client.post(reverse('staff:create_category'), data=self.category.__dict__)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Category.objects.first().id, 1)

    def test_measurement_create_get(self):
        response = self.client.get(reverse('staff:create_measurement'))
        self.assertEqual(response.status_code, 200)

    def test_measurement_create_form(self):
        form = MeasurementForm(data={'unit_shorthand': self.measurement.unit_shorthand, 'unit_fullname': self.measurement.unit_fullname})
        self.assertTrue(form.is_valid())

    def test_measurement_create_post(self):
        response = self.client.post(reverse('staff:create_measurement'), data=self.measurement.__dict__)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Measurement.objects.first().id, 1)

    def test_category_edit_get(self):
        response = self.client.get(reverse('staff:edit_category', args=[self.category.id]))
        self.assertEqual(response.status_code, 200)

    def test_category_edit_post(self):
        response = self.client.post(reverse('staff:edit_category', args=[self.category.id]), data=self.category.__dict__)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Category.objects.first().id, 1)

    def test_measurement_edit_get(self):
        response = self.client.get(reverse('staff:edit_measurement', args=[self.measurement.id]))
        self.assertEqual(response.status_code, 200)

    def test_measurement_edit_post(self):
        response = self.client.post(reverse('staff:edit_measurement', args=[self.measurement.id]), data=self.measurement.__dict__)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Measurement.objects.first().id, 1)

    def test_category_delete(self):
        response = self.client.post(reverse('staff:delete_category', args=[self.category.id]))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Category.objects.count(), 0)

    def test_measurement_delete(self):
        response = self.client.post(reverse('staff:delete_measurement', args=[self.measurement.id]))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Measurement.objects.count(), 0)
