# in your app's forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
# in your app's forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CustomRegistrationForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = User  # Use the built-in User model
        fields = ('username', 'password1', 'password2')

