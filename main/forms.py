from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from captcha.fields import CaptchaField

from main.models import *


class AddPostForm(forms.ModelForm):
    class Meta:
        model = File
        fields = "__all__"


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label="Логин", widget=forms.TextInput(attrs={"class": "form-input"}))
    email = forms.EmailField(label="Email", widget=forms.EmailInput(attrs={"class": "email-input"}))
    password1 = forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={"class": "email-input"}))
    password2 = forms.CharField(label="Пароль повтор", widget=forms.PasswordInput(attrs={"class": "email-input"}))
    captcha = CaptchaField()

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")


class LoginUserForm(AuthenticationForm):
    class Meta:
        username = forms.CharField(label="Логин", widget=forms.TextInput(attrs={"class": "form-input"}))
        password = forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={"class": "email-input"}))
        captcha = CaptchaField()