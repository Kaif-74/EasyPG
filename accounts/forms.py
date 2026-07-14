from django import forms
from django.contrib.auth.models import User
from .models import OwnerProfile

class OwnerRegistrationForm(forms.ModelForm):
    full_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Full Name'}))
    mobile_number = forms.CharField(max_length=15, widget=forms.TextInput(attrs={'placeholder': 'Mobile Number'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email Address'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}))

    class Meta:
        model = User
        fields = ['full_name', 'email', 'mobile_number', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match!")
        return cleaned_data

class ProfileForm(forms.ModelForm):
    class Meta:
        model = OwnerProfile
        fields = ['full_name', 'mobile_number']