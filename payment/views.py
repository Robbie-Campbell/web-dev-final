from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import PaymentForm
from account.models import UserBase
import stripe


from basket.basket import Basket

@login_required
def payment_home(request):
    use_data = False
    user = UserBase.objects.get(pk=request.user.id)
    basket = Basket(request)
    total = str(basket.get_total_price())
    total = total.replace('.', '')
    total = int(total)

    stripe.api_key = 'sk_test_51J0N5bBduLhIpeffiM2F2b3fAeLcX3fhcqny7g7lCbYPYCzohjhFDraawgwlTUwbmXDt2ulIxYNUurfKkRxdCZQE00Cghnqjnc'

    intent = stripe.PaymentIntent.create(
        amount=total,
        currency='gbp',
        metadata={'userid': request.user.id}
    )
    data ={'first_name': user.first_name, 'last_name': user.last_name, 'email': user.email, 
            'address_line_1': user.address_line_1, 'postcode': user.postcode,
            'town_city': user.town_city, 'country': user.country}

    nones = all(data.values())
    if nones:
        use_data = True
    if request.method == 'GET':
        use_data = False
        form = PaymentForm(data=data)
    else:
        form = PaymentForm()
    return render(request, 'payment/home.html', {'form': form, 'client_secret': intent.client_secret, 'use_data': use_data})