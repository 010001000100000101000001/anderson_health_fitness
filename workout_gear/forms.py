from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import ProductReview

class ProductReviewForm(forms.ModelForm):
    """
    Form for submitting a review for a specific gear item, with rating and comment fields.
    """
    class Meta:
        model = ProductReview
        fields = ['rating', 'comment']
        widgets = {
            'rating': forms.NumberInput(attrs={'min': 1, 'max': 5}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Initialize Crispy Forms helper
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit Review'))
