from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import GearCategory, GearItem
from .models import ProductReview

class ProductForm(forms.ModelForm):

    class Meta:
        model = GearItem
        # Exclude 'rating' from the product form as it is handled via customer reviews
        exclude = ['rating']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = GearCategory.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'


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
