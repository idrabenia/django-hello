
from django import forms


class UserForm(forms.Form):
    first_name = forms.CharField(max_length=255)
    last_name = forms.CharField(max_length=255)
    email = forms.EmailField(max_length=255, required=False)
    birth_year = forms.IntegerField(min_value=1900, max_value=2100)

    country = forms.CharField(max_length=255)
    city = forms.CharField(max_length=255)
    address1 = forms.CharField(max_length=255)
    address2 = forms.CharField(max_length=255, required=False)
    address3 = forms.CharField(max_length=255, required=False)

