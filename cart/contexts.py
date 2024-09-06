from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from workout_gear.models import GearItem

def cart_contents(request):
    """
    Context processor to handle cart contents
    """

    cart_items = []
    total = 0
    product_count = 0
    cart = request.session.get('cart', {})

    # Loop through the items in the session cart
    for item_id, item_data in cart.items():
        gear_item = get_object_or_404(GearItem, pk=item_id)
        quantity = item_data
        total += quantity * gear_item.cost
        product_count += quantity

        cart_items.append({
            'product': gear_item,
            'quantity': quantity,
            'subtotal': quantity * gear_item.cost,
        })

    # Calculate delivery cost
    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    # Calculate grand total
    grand_total = total + delivery

    context = {
        'cart_items': cart_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context
