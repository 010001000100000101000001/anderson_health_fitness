from django.shortcuts import render, redirect, get_object_or_404
from workout_gear.models import GearItem

# Create your views here.

def view_cart(request):
    """ A view that renders the cart contents page """

    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """
    Add a specified quantity of a gear item to the shopping cart.
    """
    quantity = int(request.POST.get('quantity', 1))
    redirect_url = request.POST.get('redirect_url', '/')

    # Fetch the gear item
    gear_item = get_object_or_404(GearItem, pk=item_id)

    # Fetch the cart from the session
    cart = request.session.get('cart', {})

    # Check if the item is already in the cart and update quantity
    if str(item_id) in cart:
        cart[str(item_id)]['quantity'] += quantity
    else:
        cart[str(item_id)] = {
            'quantity': quantity,
            'name': gear_item.name,
            'price': str(gear_item.cost),
            'image_url': gear_item.image_file.url if gear_item.image_file else None,
        }

    # Save the updated cart to the session
    request.session['cart'] = cart
    return redirect(redirect_url)