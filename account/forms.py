from django import forms
from .models import UserBase


class RegistrationForm(forms.ModelForm):
    username = forms.CharField(label="Enter Username", min_length=4, max_length=50, help_text="Required")
    email = forms.EmailField(label="Enter Email", min_length=4, max_length=100, error_messages={'required': 'Please enter an Email'})
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