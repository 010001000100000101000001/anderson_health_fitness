from django import forms
from .models import Order
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
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
            # CountrySelectWidget for better rendering
            'country': CountrySelectWidget(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Define placeholder text for each field
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'postcode': 'Postal Code',
            'town_or_city': 'Town or City',
            'street_address1': 'Street Address 1',
            'street_address2': 'Street Address 2',
            'county': 'County'
        }

        # Set placeholders and other attributes for each field
        for field in self.fields:
            if field != 'country':
                placeholder = (
                    f"{placeholders.get(field, '')} *"
                    if self.fields[field].required
                    else placeholders.get(field, '')
                )
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'form-control'
            self.fields[field].label = False

        # Update the 'country' field's widget attributes
        self.fields['country'].widget.attrs.update({'class': 'form-control'})

        # Crispy Forms integration for Bootstrap 5
        self.helper = FormHelper(self)
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            *self.fields.keys(),
            Submit(
                'thissubmit',
                'Complete Purchase',
            )
        )
