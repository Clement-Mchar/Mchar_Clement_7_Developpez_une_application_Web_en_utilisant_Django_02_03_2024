from django.contrib.auth import get_user_model
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, UserFollow
from django.core.exceptions import ValidationError

class SignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ['username']

class LoginForm(forms.Form):
    username = forms.CharField(max_length=63, label='Nom d’utilisateur')
    password = forms.CharField(max_length=63, widget=forms.PasswordInput, label='Mot de passe')

class FollowingForm(forms.Form):
    username = forms.CharField(max_length=100, label="nom d'utilisateur")
    
    def clean_username(self):
        data = self.cleaned_data['username']

        if User.objects.filter(username=data).exists():
            return data
        else:
            raise ValidationError("Cet utilisateur n'existe pas.")


    