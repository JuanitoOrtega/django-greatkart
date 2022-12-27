from django.forms import *
from .models import Order
from django_countries.widgets import CountrySelectWidget


class OrderForm(ModelForm):

    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'phone', 'email', 'address_line_1', 'address_line_2', 'country', 'state', 'city', 'order_note']
        widgets = {
            'country': CountrySelectWidget(
                attrs={
                    'class': 'form-control country-select-flag',
                }
            )
        }