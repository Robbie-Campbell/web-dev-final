from django.shortcuts import render
from django.http.response import JsonResponse

from basket.basket import Basket
from .models import Order, OrderItem
from payment.forms import PaymentForm

def add(request):
    basket = Basket(request)
    if request.method == "POST":
        form = PaymentForm(request.POST)
        user_id = request.user.id
        order_key = request.POST.get('order_key')
        baskettotal = basket.get_total_price()
        print(form.errors)
        if form.is_valid():
            form = form.cleaned_data
            if Order.objects.filter(order_key=order_key).exists():
                pass
            else:
                order = Order.objects.create(user_id=user_id, fullname=f"{form['first_name']} {form['last_name']}",
                                            address1=form['address_line_1'], address2=form['address_line_2'], city=form['town_city'],
                                            phone=request.user.phone_number, postcode=form['postcode'], total_paid=baskettotal, 
                                            order_key=order_key)
                order_id = order.pk
                for item in basket:
                    OrderItem.objects.create(order_id=order_id, recipe=item['recipe'], price=item['price'], quantity=item['qty'])
    response = JsonResponse({'success': 'Successfully created order information' })
    return response

def payment_confirmation(data):
    Order.objects.filter(order_key=data).update(billing_status=True)

def user_orders(request):
    user_id = request.user.id
    orders = Order.objects.filter(user_id=user_id).filter(billing_status=True)
    return orders