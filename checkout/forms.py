from django import forms
from .models import Order
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            'full_name', 'email', 'phone_number', 'country',
            'postcode', 'town_or_city', 'street_address1',
            'street_address2', 'county'
        ]
        widgets = {
            'full_name': forms.TextInput(attrs={'placeholder': 'Full Name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email Address'}),
            'phone_number': forms.TextInput(
                attrs={'placeholder': 'Phone Number'}
            ),
            'country': CountrySelectWidget(attrs={'placeholder': 'Country'}),
            'postcode': forms.TextInput(attrs={'placeholder': 'Postal Code'}),
            'town_or_city': forms.TextInput(
                attrs={'placeholder': 'Town or City'}
            ),
            'street_address1': forms.TextInput(
                attrs={'placeholder': 'Street Address 1'}
            ),
            'street_address2': forms.TextInput(
                attrs={'placeholder': 'Street Address 2'}
            ),
            'county': forms.TextInput(attrs={'placeholder': 'County'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Crispy Forms integration for Bootstrap 5
        self.helper = FormHelper(self)
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            *self.fields.keys(),
            Submit(
                'thissubmit',
                'Complete Purchase',
                css_class='btn btn-primary w-100'
            )
        )
