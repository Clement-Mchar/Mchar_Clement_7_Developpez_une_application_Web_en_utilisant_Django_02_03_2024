from django.contrib.auth import get_user_model
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User
from django.core.exceptions import ValidationError


class SignupForm(UserCreationForm):
    username = forms.CharField(
        max_length=63,
        label="",
        widget=forms.TextInput(
            attrs={"placeholder": "Nom d'utilisateur", "class": "signup-form"}
        ),
    )
    password1 = forms.CharField(
        max_length=63,
        label="",
        widget=forms.PasswordInput(
            attrs={"placeholder": "Mot de passe", "class": "signup-form"}
        ),
    )
    password2 = forms.CharField(
        max_length=63,
        label="",
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Confirmez le mot de passe",
                "class": "signup-form",
            }
        ),
    )

    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ["username"]


class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=63,
        label="",
        widget=forms.TextInput(
            attrs={"placeholder": "Nom d'utilisateur", "class": "login-form"}
        ),
    )
    password = forms.CharField(
        max_length=63,
        label="",
        widget=forms.PasswordInput(
            attrs={"placeholder": "Mot de passe", "class": "login-form"}
        ),
    )


class FollowingForm(forms.Form):
    username = forms.CharField(
        max_length=100,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Entrez un nom d'utilisateur..."}),
    )
