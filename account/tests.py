from importlib import import_module

from django.conf import settings
from django.http import HttpRequest
from django.test import Client, SimpleTestCase, TestCase
from django.urls import reverse

from orders import views
from account.models import UserBase
from payment.forms import PaymentForm
from account.forms import RegistrationForm, UserEditForm


class TestAccount(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = UserBase.objects.create(username='admin', email='test@email.com', password='test')
        self.password = 'testpass'
        self.admin = UserBase.objects.create_superuser('tester', 'myemail@test.com', self.password)

    def test_dashboard_url(self):
        self.client.login(email=self.admin.email, password=self.password)
        response = self.client.get(reverse('account:dashboard'))
        self.assertEqual(response.status_code, 200)

    def test_user_edit_post(self):
        self.client.login(email=self.admin.email, password=self.password)
        self.client.post(reverse('account:edit_profile'), 
                                 data={'id':1,'first_name':'test', 'last_name':'test', 'email':'test@email.com', 'address_line_1':'test',
                                 'postcode':'test', 'town_city': 'test', 'country':'GB'})
        response = self.client.get(reverse('account:edit_profile'))
        self.assertEqual(response.status_code, 200)
    
    def test_user_delete(self):
        self.client.login(email=self.admin.email, password=self.password)
        response = self.client.post(reverse('account:delete_profile'))
        self.assertEqual(response.status_code, 302)

    def test_user_create_redirect(self):
        self.client.login(email=self.admin.email, password=self.password)
        response = self.client.get(reverse('account:register'))
        self.assertRedirects(response, '/', status_code=302, 
                             target_status_code=200, fetch_redirect_response=True)

    def test_user_create_get(self):
        self.client.logout()
        response = self.client.get(reverse('account:register'))
        self.assertEqual(response.status_code, 200)

    def test_registration_view(self):
        response = self.client.post(reverse('account:register'),
                                    data={ 'username': 'alice', # Will fail on username uniqueness.
                                           'email': 'foo@example.com',
                                           'password1': 'foo',
                                           'password2': 'foo' })
        self.assertEqual(response.status_code, 302)

        response = self.client.post(reverse('account:register'),
                                    data={ 'username': 'foo',
                                           'email': 'foo@example.com',
                                           'password1': 'foo',
                                           'password2': 'foo' })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(UserBase.objects.count(), 3)