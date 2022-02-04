from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from main.models import *


class AddPostForm(forms.ModelForm):
    class Meta:
        model = File
        fields = "__all__"


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label="логин", widget=forms.TextInput(attrs={"class": "form-input"}))
    email = forms.EmailField(label="Email", widget=forms.EmailInput(attrs={"class": "email-input"}))
    password1 = forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={"class": "email-input"}))
    password2 = forms.CharField(label="Пароль повтор", widget=forms.PasswordInput(attrs={"class": "email-input"}))

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
