from django.shortcuts import render, get_object_or_404
from .models import GearCategory, GearItem
from django.db.models import Q


def gear_list(request):
    categories = GearCategory.objects.all()
    gear_items = GearItem.objects.all()

    context = {
        'categories': categories,
        'gear_items': gear_items,
    }
    return render(request, 'workout_gear/workout_gear.html', context)


def category_gear_list(request, category_id):
    category = get_object_or_404(GearCategory, pk=category_id)
    gear_items = GearItem.objects.filter(category=category)
    context = {
        'category': category,
        'gear_items': gear_items,
    }
    return render(request, 'workout_gear/category_gear_list.html', context)


def gear_detail(request, item_id):
    gear_item = get_object_or_404(GearItem, pk=item_id)
    context = {
        'gear_item': gear_item,
    }
    return render(request, 'workout_gear/gear_detail.html', context)


def search_gear(request):
    query = request.GET.get('q')
    gear_items = GearItem.objects.filter(Q(name__icontains=query) | Q(details__icontains=query))

    context = {
        'query': query,
        'gear_items': gear_items,
    }
    return render(request, 'workout_gear/search_results.html', context)