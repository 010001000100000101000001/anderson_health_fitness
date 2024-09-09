from django.shortcuts import render, redirect, get_object_or_404
from workout_gear.models import GearItem

# Create your views here.

def view_cart(request):
    """ A view that renders the cart contents page
        and displays all items in the cart.
    """

    # Retrieve the cart from the session
    cart = request.session.get('cart', {})
    cart_items = []

    # Loop through items in the cart and prepare them for rendering
    for item_id, item_data in cart.items():
        gear_item = get_object_or_404(GearItem, pk=item_id)
        cart_items.append({
            'product': gear_item,
            'quantity': item_data['quantity'],
            'subtotal': gear_item.cost * item_data['quantity'],
        })

    # Prepare the context
    context = {
        'cart_items': cart_items,
    }

    return render(request, 'cart/cart.html', context)


def add_to_cart(request, item_id):
    """
    Add a specified quantity of a gear item to the shopping cart.
    """
    quantity = int(request.POST.get('quantity', 1)) # Default to 1 if not specified
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
    return redirect('redirect_url')


# Update the quantity of an item in the cart
def update_cart(request, item_id):
    """
    Update the quantity of a specific item in the shopping cart.
    """
    quantity = int(request.POST.get('quantity'))

    # Fetch the cart from the session
    cart = request.session.get('cart', {})

    if str(item_id) in cart:
        if quantity > 0:
            cart[str(item_id)]['quantity'] = quantity
        else:
            # Remove the item if quantity is zero
            cart.pop(str(item_id))

    # Save the updated cart to the session
    request.session['cart'] = cart
    return redirect('view_cart')
