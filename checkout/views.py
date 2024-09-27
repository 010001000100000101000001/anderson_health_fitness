from django.conf import settings
from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from .forms import OrderForm
from .models import Order, OrderLineItem
from workout_gear.models import GearItem
from cart.contexts import cart_contents
from decimal import Decimal
import stripe
import json

@require_POST
def cache_checkout_data(request):
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'cart': json.dumps(request.session.get('cart', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Sorry, your payment cannot be \
            processed right now. Please try again later.')
        return HttpResponse(content=e, status=400)


def checkout(request):
    """
    A view to handle the checkout page and display the order form.
    """
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    stripe_currency = settings.STRIPE_CURRENCY

    cart = request.session.get('cart', {})

    # If the cart is empty, show an error and redirect back to products page
    if not cart:
        messages.error(request, "Your cart is currently empty.")
        return redirect(reverse('workout_gear_list'))

    if request.method == 'POST':
        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'country': request.POST['country'],
            'postcode': request.POST['postcode'],
            'town_or_city': request.POST['town_or_city'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'county': request.POST['county'],
        }
        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save()
            for item_id, item_data in cart.items():
                try:
                    gear_item = get_object_or_404(GearItem, pk=int(item_id))
                    order_line_item = OrderLineItem(
                        order=order,
                        product=gear_item,
                        quantity=item_data['quantity'],
                    )
                    order_line_item.save()
                except GearItem.DoesNotExist:
                    messages.error(request, "One of the items in your cart was not found in our database.")
                    order.delete()
                    return redirect(reverse('view_cart'))
            
            # Clear the cart from the session
            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('checkout_success', args=[order.order_number]))
        else:
            messages.error(request, 'There was an error with your form. Please double-check your information.')

    # GET request: Set up the Stripe payment intent and context
    current_cart = cart_contents(request)
    total = Decimal(current_cart['grand_total'])
    stripe_total = round(total * 100)
    stripe.api_key = stripe_secret_key

    # Create the PaymentIntent object for the transaction
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=stripe_currency,
    )

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)


def checkout_success(request, order_number):
    """
    Handle successful checkouts
    """
    order = get_object_or_404(Order, order_number=order_number)
    messages.success(request, f'Order successfully processed! Your order number is {order_number}. A confirmation email will be sent to {order.email}.')

    # Clear the cart from the session
    if 'cart' in request.session:
        del request.session['cart']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)
