from django.conf import settings
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, request
from django.contrib import messages
from .models import User, UserFollow
from .forms import FollowingForm

from . import forms


# Create your views here.
def sign(request):
    if request.user.is_authenticated:
        return redirect('flux')
    form = forms.LoginForm(request.POST if request.method == 'POST' else None)
    if request.method == 'POST' and form.is_valid():
        user = authenticate(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password'],
        )
        if user is not None:
            login(request, user)
            messages.success(request, 'bravo chakal')
            return redirect(settings.LOGIN_REDIRECT_URL)
        else:
            messages.error(request, "Identifiants invalides")
    return render(request, 'app/sign.html', locals())

@login_required
def welcome():
    return redirect('flux')

def sign_up(request):
    if request.user.is_authenticated:
        return redirect('flux')
    form = forms.SignupForm(request.POST if request.method == 'POST' else None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
    return render(request, 'app/sign-up.html', context={'form': form})

def logout_user(request):

    logout(request)
    return redirect('sign')

@login_required
def follow_user(request):
    form = FollowingForm(request.POST if request.method == 'POST' else None)
    followings = UserFollow.objects.all()
    if request.method == 'POST':
        if form.is_valid():
            UserFollow.objects.create(user=request.user, followed_user=User.objects.get(username__iexact=form.cleaned_data['username']))
            return redirect('followings')
    return render(request, 'app/followings.html', {'form':form, 'followings':followings})