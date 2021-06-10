from django import forms
from .models import UserBase
from django_countries.fields import CountryField
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm, SetPasswordForm


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control mb-3', 'placeholder': 'Username', 'id': 'login-username'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Password',
            'id': 'login-pwd',
        }
    ))


class RegistrationForm(forms.ModelForm):
    username = forms.CharField(label="Enter Username", required=True, min_length=4, max_length=50)
    email = forms.EmailField(label="Enter Email", min_length=4, max_length=100, required=True, error_messages={'required': 'Please enter an Email'})
    password1 = forms.CharField(label="Enter Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repeat Password", widget=forms.PasswordInput)

    class Meta:
        model = UserBase
        fields = ("username", "email",)

    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        r = UserBase.objects.filter(username=username)
        if r.count():
            raise forms.ValidationError("Username already exists")
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        r = UserBase.objects.filter(email=email)
        if r.count():
            raise forms.ValidationError("Email already exists")
        return email

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] != cd['password2']:
            raise forms.ValidationError('Passwords do not match.')
        return cd['password2']

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


class UserEditForm(forms.ModelForm):
    email = forms.EmailField(
        label='Account Email (Cannot be changed)', max_length=100, disabled=True, widget=forms.TextInput(
            attrs={'class': 'form-control mb-2', 'placeholder': 'Email', 'id': 'form-email', 'readonly': 'readonly'}))

    username = forms.CharField(
        label='Username', max_length=100, disabled=True, widget=forms.TextInput(
            attrs={'class': 'form-control mb-2', 'placeholder': 'Username', 'id': 'form-username', 'readonly': 'readonly'}))

    first_name = forms.CharField(
        label='First Name', max_length=100, required=False, widget=forms.TextInput(
            attrs={'class': 'form-control mb-2', 'placeholder': 'First Name', 'id': 'form-firstname'}))

    last_name = forms.CharField(
        label='Last Name', max_length=100, required=False, widget=forms.TextInput(
            attrs={'class': 'form-control mb-2', 'placeholder': 'Last Name', 'id': 'form-lastname'}))

    phone_number = forms.CharField(
        label='Phone Number', max_length=100, required=False, widget=forms.TextInput(
            attrs={'class': 'form-control mb-2', 'placeholder': 'Phone Number', 'id': 'form-phone'}))

    address_line_1 = forms.CharField(
        label='Address Line 1', max_length=100, required=False, widget=forms.TextInput(
            attrs={'class': 'form-control mb-2', 'placeholder': 'Add Ln 1', 'id': 'form-add1'}))

    address_line_2 = forms.CharField(
        label='Address Line 2', max_length=100, required=False, widget=forms.TextInput(
            attrs={'class': 'form-control mb-2', 'placeholder': 'Add Ln 2', 'id': 'form-add2'}))

    postcode = forms.CharField(
        label='Postcode', max_length=100, required=False, widget=forms.TextInput(
            attrs={'class': 'form-control mb-2', 'placeholder': 'postcode', 'id': 'form-postcode'}))

    town_city = forms.CharField(
        label='Town / City', max_length=100, required=False, widget=forms.TextInput(
            attrs={'class': 'form-control mb-2', 'placeholder': 'Town / City', 'id': 'form-towncity'}))

    country = CountryField().formfield()

    class Meta:
        model = UserBase
        fields = ('email', 'username', 'first_name', 'last_name', 'phone_number', 'address_line_1', 'address_line_2', 'postcode', 'town_city', 'country')

    def __init__(self, *args, **kwargs):
        super(UserEditForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            self.fields['username'].required = True
            self.fields['email'].required = True


class PwdResetForm(PasswordResetForm):
    email = forms.EmailField(
        max_length=100, widget=forms.TextInput(
            attrs={'class': 'form-control mb-2', 'placeholder': 'Email', 'id': 'form-email'}))

    def clean_email(self):
        email = self.cleaned_data['email']
        u = UserBase.objects.get(email=email)
        if not u:
            raise forms.ValidationError(
                "We cannot find that email address."
            )
        return email


class PwdResetConfirmForm(SetPasswordForm):
    new_password1 = forms.CharField(
        label='New Password', max_length=100, widget=forms.PasswordInput(
            attrs={'class': 'form-control mb-2', 'placeholder': 'New Password', 'id': 'form-new-pass1'}))

    new_password2 = forms.CharField(
        label='Repeat Password', max_length=100, widget=forms.PasswordInput(
            attrs={'class': 'form-control mb-2', 'placeholder': 'Repeat Password', 'id': 'form-new-pass2'}))
