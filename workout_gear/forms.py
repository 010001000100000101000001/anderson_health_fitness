from django import forms
from .models import ProductReview

class ProductReviewForm(forms.ModelForm):
    """
    Form for submitting a review for a specific gear item.
    """
    class Meta:
        model = ProductReview
        fields = ['rating', 'comment']
        widgets = {
            'rating': forms.NumberInput(attrs={'min': 1, 'max': 5}),
        }
