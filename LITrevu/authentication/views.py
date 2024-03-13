from django.conf import settings
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, request
from django.contrib import messages

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
def welcome(request):
    return redirect('flux')

def sign_up(request):
    form = forms.SignupForm(request.POST if request.method == 'POST' else None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success('bravo')
    return render(request, 'app/sign-up.html', context={'form': form})

def logout_user(request):

    logout(request)
    return redirect('sign')
    