from django import forms

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class CreateUserForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"class" : "text-input", "placeholder":"Enter Student ID"}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={"class" : "text-input", "placeholder":"Enter First Name"}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={"class" : "text-input", "placeholder":"Enter Last Name"}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class" : "text-input", "placeholder":"Enter Password"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class" : "text-input", "placeholder":"Confirm Password"}))


    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password1', 'password2']
