from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class RegistartionForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', "last_name", "password1", "password2"]

class EditProfileForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', "last_name"]