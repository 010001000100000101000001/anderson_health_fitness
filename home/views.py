from django.shortcuts import render
from django.contrib import messages
from .forms import NewsletterSignupForm


def index(request):
    """ A view to return the index page """
    if request.method == "POST":
        form = NewsletterSignupForm(request.POST)
        if form.is_valid():
            # Simulated success (no Mailchimp integration)
            email = form.cleaned_data['email']
            messages.success(
                request, f"Thank you for signing up with {email}!"
                )
        else:
            messages.error(request, "Please enter a valid email address.")
    else:
        form = NewsletterSignupForm()

    context = {
        'form': form,
    }
    return render(request, 'home/index.html', context)
