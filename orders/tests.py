from importlib import import_module

from django.conf import settings
from django.http import HttpRequest
from django.test import Client, SimpleTestCase, TestCase
from django.urls import reverse

from orders import views
from account.models import UserBase
from payment.forms import PaymentForm
from basket.basket import Basket
from orders.models import Order, OrderItem
from recipe.models import Category, Recipe


class TestOrders(TestCase):

    def setUp(self):
        self.client = Client()
        self.basket = Basket(self.client)
        self.user = UserBase.objects.create(username='admin', email='test@email.com', password='test')
        password = 'testpass'
        admin = UserBase.objects.create_superuser('tester', 'myemail@test.com', password)
        self.client.login(email=admin.email, password=password)
        self.category = Category.objects.create(title='django')
        self.recipe = Recipe.objects.create(id=1, category=self.category, title='django beginners', description="lorem", author=self.user, published=False, price='20.00', image='default.png', method="lorem")

    def test_user_add_order(self):
        self.basket.add(self.recipe, 2)
        response = self.client.post(reverse('orders:add'), {'id':1,'first_name':'test', 'last_name':'test', 'email':'test@email.com', 'address_line_1':'test',
                                   'postcode':'test', 'town_city': 'test', 'country':"GB", 'order_key': 'test', 'total_paid':200.00}, request=self.client, basket=self.basket)
        self.assertEquals(response.status_code, 200)
        self.assertEqual(Order.objects.first().id, 1)

    def test_payment_form(self):
        form = PaymentForm(data={'first_name':'test', 'last_name':'test', 'email':'test@email.com', 'address_line_1':'test',
                           'postcode':'test', 'town_city': 'test', 'country':"GB"})
        self.assertTrue(form.is_valid())

    def test_payment_confirmation(self):
        order = Order.objects.create(id=1, user=self.user, fullname='test', address1='test',
                                     postcode='test', city= 'test', phone="12754123", order_key= 'test', total_paid=200.00, billing_status=False)
        views.payment_confirmation(order.order_key)
        order.refresh_from_db()
        self.assertEquals(order.billing_status, True)

    def test_user_orders(self):
        self.assertEquals(views.user_orders(self).count(), 0)
