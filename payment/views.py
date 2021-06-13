
import json
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import PaymentForm
from django.views.decorators.csrf import csrf_exempt
from account.models import UserBase
from orders.views import payment_confirmation
import stripe
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from basket.basket import Basket
from django.http.response import HttpResponse


@login_required
def payment_home(request):
    use_data = False
    user = UserBase.objects.get(pk=request.user.id)
    basket = Basket(request)
    total = str(basket.get_total_price())
    total = total.replace('.', '')
    total = int(total)

    stripe.api_key = ''

    intent = stripe.PaymentIntent.create(
        amount=total,
        currency='gbp',
        metadata={'userid': request.user.id}
    )
    data = {'first_name': user.first_name, 'last_name': user.last_name, 'email': user.email,
            'address_line_1': user.address_line_1, 'postcode': user.postcode,
            'town_city': user.town_city, 'country': user.country}

    nones = all(data.values())
    if nones:
        use_data = True
    if 'populate' in request.GET:
        use_data = False
        form = PaymentForm(data=data)
    else:
        form = PaymentForm()
    return render(request, 'payment/home.html', {'form': form, 'client_secret': intent.client_secret, 'use_data': use_data})


@csrf_exempt
def stripe_webhook(request):
    payload = request.body
    event = None
    print("hello")

    try:
        event = stripe.Event.construct_from(
            json.loads(payload), stripe.api_key
        )
    except ValueError as e:
        print(e)
        return HttpResponse(status=400)

    # Handle the event
    if event.type == 'payment_intent.succeeded':
        payment_confirmation(event.data.object.client_secret)

    else:
        print('Unhandled event type {}'.format(event.type))

    return HttpResponse(status=200)

@login_required
def order_placed(request):
    basket = Basket(request)
    basket.clear()
    user = request.user
    current_site = get_current_site(request)
    subject = 'Your Order has been placed!'
    message = render_to_string('payment/orderplaced_email.html', {
        'user': user,
        'domain': current_site.domain,
    })
    user.email_user(subject=subject, message=message)
    return render(request, 'payment/orderplaced.html')
