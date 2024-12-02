from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import NewsletterSignupForm

def index(request):
    """ A view to return the index page """
    if request.method == "POST":
        form = NewsletterSignupForm(request.POST)
        if form.is_valid():
            # Simulate saving the email or sending it to a mailing list service
            email = form.cleaned_data['email']
            messages.success(request, f"Thank you for signing up with {email}!")
        else:
            messages.error(request, "Please enter a valid email address.")
    else:
        form = NewsletterSignupForm()

    context = {
        'form': form,
    }
    return render(request, 'home/index.html', context)

def subscribe(request):
    """ A view to handle newsletter subscription """
    if request.method == "POST":
        form = NewsletterSignupForm(request.POST)
        if form.is_valid():
            # Simulate saving the email or sending it to a mailing list service
            messages.success(request, "Thank you for subscribing!")
        else:
            messages.error(request, "Please enter a valid email address.")
    return redirect('home')