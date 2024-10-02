from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q, Avg
from .models import GearCategory, GearItem, ProductReview
from .forms import ProductReviewForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages


def gear_list(request):
    """
    Displays a list of all gear items along with their categories,
    including sorting.
     """
    categories = GearCategory.objects.all()
    gear_items = GearItem.objects.all()
    sort = None
    direction = None

    # Check for sorting in the GET request
    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                gear_items = gear_items.order_by('name')
            elif sortkey == 'price':
                gear_items = gear_items.order_by('cost')
            elif sortkey == 'rating':
                gear_items = gear_items.order_by('rating')
            elif sortkey == 'category':
                gear_items = gear_items.order_by('category__name')

                # Handle sorting direction
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    gear_items = gear_items.reverse()

    current_sorting = f'{sort}_{direction}'

    # Pass the categories and gear items to the template
    context = {
        'categories': categories,
        'gear_items': gear_items,
        'current_sorting': current_sorting,

    }
    return render(request, 'workout_gear/workout_gear.html', context)


def category_gear_list(request, category_id):
    """
    Displays all gear items belonging to a specific category.
    """

    # Get the selected category based on the category_id from the URL
    category = get_object_or_404(GearCategory, pk=category_id)

    # Filter the gear items based on the selected category
    gear_items = GearItem.objects.filter(category=category)

    # Pass the category and gear items to the template
    context = {
        'category': category,
        'gear_items': gear_items,
    }
    return render(request, 'workout_gear/category_gear_list.html', context)


def gear_detail(request, item_id):
    """
    Displays detailed information about a specific gear item,
    including user reviews.
    """
    # Get the specific gear item based on the item_id from the URL
    gear_item = get_object_or_404(GearItem, pk=item_id)

    # Get all reviews associated with this gear item
    reviews = ProductReview.objects.filter(gear_item=gear_item)
    average_rating = reviews.aggregate(
        avg_rating=Avg('rating'))['avg_rating'] or 0

    form = ProductReviewForm()

    context = {
        'gear_item': gear_item,
        'reviews': reviews,
        'average_rating': average_rating,
        'form': form,
    }
    return render(request, 'workout_gear/gear_detail.html', context)


def search_gear(request):
    """
    Handles the search functionality,
    allowing users to search for gear items by name or description.
    """
    # Get the search query from the request's GET parameters
    query = request.GET.get('q')

    # If there's a query, filter the gear items by name or details
    if query:
        gear_items = GearItem.objects.filter(
            Q(name__icontains=query) | Q(details__icontains=query)
        )
    else:
        gear_items = GearItem.objects.all()  # Show all items if no query

    # Pass the search query and filtered gear items to the template
    context = {
        'query': query,
        'gear_items': gear_items,
    }
    return render(request, 'workout_gear/search_results.html', context)


@login_required
def submit_review(request, item_id):
    """
    Allows authenticated users to submit a review for a gear item.
    """
    gear_item = get_object_or_404(GearItem, pk=item_id)

    # Check if the user has already submitted a review for this item
    existing_review = ProductReview.objects.filter(
        gear_item=gear_item,
        user=request.user
        ).first()

    if existing_review:
        messages.error(request, "You have already reviewed this product.")
        return redirect('gear_detail', item_id=item_id)

    if request.method == 'POST':
        form = ProductReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.gear_item = gear_item
            review.user = request.user
            review.save()
            messages.success(
                request,
                "Your review has been submitted successfully.")
            return redirect('gear_detail', item_id=item_id)
    else:
        form = ProductReviewForm()

    # Pass the form and gear item to the template for review submission
    context = {
        'form': form,
        'gear_item': gear_item,
    }
    return render(request, 'workout_gear/submit_review.html', context)
