from django.shortcuts import render
from .models import GearCategory, GearItem

def gear_list(request):
    categories = GearCategory.objects.all()
    gear_items = GearItem.objects.all()

    context = {
        'categories': categories,
        'gear_items': gear_items,
    }
    return render(request, 'workout_gear/workout_gear.html', context)
