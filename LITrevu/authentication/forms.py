from django.contrib.auth import get_user_model
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, UserFollow
class SignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ['username']
        labels = {'username': ("Nom d'utilisateur")}

class LoginForm(forms.Form):
    username = forms.CharField(max_length=63, label='Nom d’utilisateur')
    password = forms.CharField(max_length=63, widget=forms.PasswordInput, label='Mot de passe')

class FollowingForm(forms.ModelForm):
    username = forms.CharField(max_length=100, label="nom d'utilisateur")
    
    class Meta:
        model = UserFollow
        exclude = ('user', 'followed_user',)