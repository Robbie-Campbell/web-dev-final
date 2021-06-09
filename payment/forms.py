from django import forms
from account.models import UserBase
from django_countries.fields import CountryField
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm, SetPasswordForm

class PaymentForm(forms.Form):
    first_name = forms.CharField(
        label='First Name', max_length=100, widget=forms.TextInput(
            attrs={'class':'form-control mb-2', 'placeholder':'First Name', 'id':'form-firstname'}))

    last_name = forms.CharField(
        label='Last Name', max_length=100, widget=forms.TextInput(
            attrs={'class':'form-control mb-2', 'placeholder':'Last Name', 'id':'form-lastname'}))

    email = forms.EmailField(
        label='Shipping Email', max_length=100, widget=forms.TextInput(
            attrs={'class':'form-control mb-2', 'placeholder':'Email', 'id':'form-email'}))

    address_line_1 = forms.CharField(
        label='Address Line 1', max_length=100, widget=forms.TextInput(
            attrs={'class':'form-control mb-2', 'placeholder':'Add Ln 1', 'id':'form-add1'}))

    address_line_2 = forms.CharField(
        label='Address Line 2', max_length=100, required=False, widget=forms.TextInput(
            attrs={'class':'form-control mb-2', 'placeholder':'Add Ln 2', 'id':'form-add2'}))

    postcode = forms.CharField(
        label='Postcode', max_length=100, widget=forms.TextInput(
            attrs={'class':'form-control mb-2', 'placeholder':'postcode', 'id':'form-postcode'}))

    town_city = forms.CharField(
        label='Town / City', max_length=100, widget=forms.TextInput(
            attrs={'class':'form-control mb-2 border-bottom', 'placeholder':'Town / City', 'id':'form-towncity'}))

    country = CountryField().formfield()