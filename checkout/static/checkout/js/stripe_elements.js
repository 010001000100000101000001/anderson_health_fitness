var stripe_public_key = document.getElementById('id_stripe_public_key').textContent.trim();
var client_secret = document.getElementById('id_client_secret').textContent.trim();

var stripe = Stripe(stripe_public_key);
var elements = stripe.elements();

var style = {
    base: {
        color: '#000',
        fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '16px',
        '::placeholder': {
            color: '#aab7c4',
        }
    },
    invalid: {
        color: '#dc3545',
        iconColor: '#dc3545',
    }
};

var card = elements.create('card', {style: style});
card.mount('#card-element');

// Handle form submission and confirm payment
var form = document.getElementById('payment-form');

form.addEventListener('submit', function(event) {
    event.preventDefault();

    stripe.confirmCardPayment(client_secret, {
        payment_method: {
            card: card,
            billing_details: {
                name: form.querySelector('input[name=full_name]').value,
                email: form.querySelector('input[name=email]').value,
            },
        }
    }).then(function(result) {
        if (result.error) {
            // Display error.message in your UI
            var errorElement = document.getElementById('card-errors');
            errorElement.textContent = result.error.message;
        } else {
            if (result.paymentIntent.status === 'succeeded') {
                // Payment succeeded
                form.submit();
            }
        }
    });
});
