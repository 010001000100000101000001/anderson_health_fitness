from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from workout_gear.models import GearItem

def cart_contents(request):
    """
    Context processor to handle cart contents
    """

    cart_items = []
    total = Decimal(0)  # Initialize total as Decimal
    product_count = 0
    cart = request.session.get('cart', {})

    # Loop through the items in the session cart
    for item_id, item_data in cart.items():
        # Convert item_id back to an integer when querying the database
        gear_item = get_object_or_404(GearItem, pk=int(item_id))
        quantity = item_data['quantity']
        cost = Decimal(gear_item.cost)  # Ensure cost is a Decimal
        subtotal = cost * quantity  # Do the multiplication using Decimal

        total += subtotal
        product_count += quantity

        # Handling image URLs
        image_url = gear_item.image_file.url if gear_item.image_file else '/media/gear_images/placeholder-for-no-product-image.webp'

        cart_items.append({
            'product_name': gear_item.name,
            'quantity': quantity,
            'subtotal': float(subtotal),  # Convert subtotal to float for serialisation
            'image_url': image_url,
        })

    # Calculate delivery cost
    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE) / 100  # Keep as Decimal
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = Decimal(0)
        free_delivery_delta = Decimal(0)

    # Calculate grand total
    grand_total = total + delivery

    # Return context data, but make sure to convert Decimals to float for session storage or templates
    context = {
        'cart_items': cart_items,
        'total': float(total),  # Convert to float for serialisation
        'product_count': product_count,
        'delivery': float(delivery),  # Convert to float
        'free_delivery_delta': float(free_delivery_delta),  # Convert to float
        'free_delivery_threshold': float(settings.FREE_DELIVERY_THRESHOLD),  # Convert to float
        'grand_total': float(grand_total),  # Convert to float
    }

    return context
