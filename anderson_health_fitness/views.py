from django.shortcuts import render


def handler404(request, exception):
    """Renders the custom 404 error page."""
    return render(request, "errors/404.html", status=404)
