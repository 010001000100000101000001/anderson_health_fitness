from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm


def checkout(request):
    """
    A view to handle the checkout page and display the order form.
    """
    cart = request.session.get('cart', {})

    # If the cart is empty, show an error and redirect back to products page
    if not cart:
        messages.error(request, "Your cart is currently empty.")
        return redirect(reverse('workout_gear_list'))

    # If there are items in the cart, display the order form
    order_form = OrderForm()

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
    }

    return render(request, template, context)
