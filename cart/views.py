from django.shortcuts import render, redirect, get_object_or_404
from workout_gear.models import GearItem
from django.contrib import messages
from .contexts import cart_contents


# View to render the cart contents page
def view_cart(request):
    """A view that renders the cart contents page and displays
        all items in the cart.
    """

    # Retrieve the cart from the session
    cart = request.session.get('cart', {})
    cart_items = []
    cart_total = 0

    # Loop through items in the cart and prepare them for rendering
    for item_id, item_data in cart.items():
        gear_item = get_object_or_404(GearItem, pk=item_id)
        subtotal = gear_item.cost * item_data['quantity']
        cart_total += subtotal
        cart_items.append({
            'item_id': item_id,
            'product': gear_item,
            'product_name': gear_item.name,
            'quantity': item_data['quantity'],
            'subtotal': subtotal,
            'image_url': (
                gear_item.image_file.url if gear_item.image_file else
                '/media/gear_images/placeholder-for-no-product-image.webp'
                ),
        })

    # Prepare the context
    context = {
        'cart_items': cart_items,
        'cart_total': cart_total,
    }

    return render(request, 'cart/cart.html', context)


def add_to_cart(request, item_id):
    """Add a specified quantity of a gear item to the shopping cart."""

    quantity = int(request.POST.get('quantity', 1))
    redirect_url = request.POST.get('redirect_url', '/')
    gear_item = get_object_or_404(GearItem, pk=item_id)
    cart = request.session.get('cart', {})

    # Add or update item in cart
    if str(item_id) in cart:
        cart[str(item_id)]['quantity'] += quantity
    else:
        cart[str(item_id)] = {
            'quantity': quantity,
            'name': gear_item.name,
            'price': str(gear_item.cost),
            'image_url': (
                gear_item.image_file.url if gear_item.image_file else
                '/media/gear_images/placeholder-for-no-product-image.webp'
                ),
        }
    messages.success(request, f'Added {gear_item.name} to cart.')

    # Save updated cart to session
    request.session['cart'] = cart

    # Retrieve cart contents for toast notifications
    cart_data = cart_contents(request)
    request.session['cart_items'] = cart_data['cart_items']
    request.session['total'] = cart_data['total']
    request.session['free_delivery_delta'] = cart_data['free_delivery_delta']

    return redirect(redirect_url)


def update_cart(request, item_id):
    """Update the quantity of a specific item in the shopping cart."""

    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if str(item_id) in cart:
        if quantity > 0:
            cart[str(item_id)]['quantity'] = quantity
            cart[str(item_id)]['image_url'] = (
                get_object_or_404(GearItem, pk=item_id).image_file.url
                if get_object_or_404(GearItem, pk=item_id).image_file else
                '/media/gear_images/placeholder-for-no-product-image.webp'
            )
            messages.success(request, 'Cart updated successfully.')
        else:
            cart.pop(str(item_id))
            messages.info(request, 'Item removed from cart.')

    # Save updated cart to session
    request.session['cart'] = cart

    # Retrieve cart contents for toast notifications
    cart_data = cart_contents(request)
    request.session['cart_items'] = cart_data['cart_items']
    request.session['total'] = cart_data['total']
    request.session['free_delivery_delta'] = cart_data['free_delivery_delta']

    return redirect('view_cart')


def remove_from_cart(request, item_id):
    """Remove a gear item from the shopping cart."""

    cart = request.session.get('cart', {})

    if str(item_id) in cart:
        cart.pop(str(item_id))
        messages.success(request, 'Item removed from cart.')
    else:
        messages.error(request, 'Item not found in cart.')

    # Save updated cart to session
    request.session['cart'] = cart

    # Retrieve cart contents for toast notifications
    cart_data = cart_contents(request)
    request.session['cart_items'] = cart_data['cart_items']
    request.session['total'] = cart_data['total']
    request.session['free_delivery_delta'] = cart_data['free_delivery_delta']

    return redirect('view_cart')
