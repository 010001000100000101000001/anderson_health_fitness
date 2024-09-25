import stripe
from django.conf import settings
from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm
from cart.contexts import cart_contents
from decimal import Decimal


def checkout(request):
    """
    A view to handle the checkout page and display the order form.
    """
    cart = request.session.get('cart', {})

    # Get Stripe keys and currency from settings
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    stripe_currency = settings.STRIPE_CURRENCY

    # If the cart is empty, show an error and redirect back to products page
    if not cart:
        messages.error(request, "Your cart is currently empty.")
        return redirect(reverse('workout_gear_list'))

    # Get the current cart contents and calculate the total
    current_cart = cart_contents(request)
    total = Decimal(current_cart['grand_total'])
    stripe_total = round(total * 100)

    # Set the Stripe secret key for the current session
    stripe.api_key = stripe_secret_key

    # Create the PaymentIntent object for the transaction
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=stripe_currency,  # Use the currency from settings
    )

    # Initialize the order form
    order_form = OrderForm()

    # If no public key is found, display a warning
    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. Did you forget to set it in your environment?')

    # Context to pass into the template
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,  # Pass the Stripe client secret
    }

    return render(request, template, context)
