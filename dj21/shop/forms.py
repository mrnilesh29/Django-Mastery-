from django import forms

from .models import Customer


class CustomerForm(forms.Form):
    class Meta:
        model = Customer
        fields = ('first_name', 'last_name', 'email', 'phone_number')

