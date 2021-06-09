from . import views
from django.urls import path

app_name = "payment"

urlpatterns = [
    path('', views.payment_home, name="payment_home"),
    path('orderplaced/', views.order_placed, name='order_placed'),
    path('webhook/', views.stripe_webhook),
]
