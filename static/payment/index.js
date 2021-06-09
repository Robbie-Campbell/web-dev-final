var stripe = Stripe('pk_test_51J0N5bBduLhIpeffssqgXweMsI5rVa3bRwRHbNtehgFlOrZHr7ZjYGiAtC6S5DTTln9FokqHnKdyv9pZxQbU8vjL00C6EtsPbo');

var elem = document.getElementById('submit');
var clientsecret = elem.getAttribute('data-secret');

var elements = stripe.elements();

var style = {
    base: {
        color: '#000',
        lineheight: '2.4',
        fontSize: '16px'
    }
}

var card = elements.create("card", {style: style})
card.mount('#card-element')

card.on('change', function(event) {
    var displayError = document.getElementById('card-errors')
    if (event.error) {
      displayError.textContent = event.error.message;
      $('#card-errors').addClass('alert alert-info');
    } else {
      displayError.textContent = '';
      $('#card-errors').removeClass('alert alert-info');
    }
});

var form = document.getElementById('payment-form');

form.addEventListener('submit', function(ev) {
    ev.preventDefault();
    
    var custFirstName = document.getElementById("form-firstname").value;
    var custLastName = document.getElementById("form-lastname").value;
    var email = document.getElementById("form-email").value;
    var custAdd1 = document.getElementById("form-add1").value;
    var custAdd2 = document.getElementById("form-add2").value;
    var postcode = document.getElementById("form-postcode").value;
    var town_city = document.getElementById("form-towncity").value;
    var postcode = document.getElementById("form-postcode").value;
    var country = document.getElementsByName("country")[0].value;

        $.ajax({
        type: "POST",
        url: 'http://127.0.0.1:8000/orders/add/',
        data: {
            first_name: custFirstName,
            last_name: custLastName,
            email:email,
            address_line_1: custAdd1,
            address_line_2: custAdd2,
            postcode: postcode,
            town_city: town_city,
            country: country,
            order_key: clientsecret,
            csrfmiddlewaretoken: CSRF_TOKEN,
            action: "post",
        },
        success: function (json) {
            console.log(json.success)
    
            stripe.confirmCardPayment(clientsecret, {
            payment_method: {
                card: card,
                billing_details: {
                address:{
                    line1:custAdd1,
                    line2:custAdd2
                },
                name: custFirstName
                },
            }
            }).then(function(result) {
            if (result.error) {
                console.log('payment error')
                console.log(result.error.message);
            } else {
                if (result.paymentIntent.status === 'succeeded') {
                console.log('payment processed')
                window.location.replace("http://127.0.0.1:8000/payment/orderplaced/");
                }
            }
            });
    
        },
        error: function (xhr, errmsg, err) {},
        });
    
}); 