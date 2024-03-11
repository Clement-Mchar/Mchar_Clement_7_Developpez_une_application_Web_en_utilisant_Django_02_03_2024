from django.conf import settings
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, request

from . import forms


# Create your views here.
def homepage(request):
    render(request, 'app/base.html')
    form = forms.LoginForm()
    message = ''
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                return redirect(settings.LOGIN_REDIRECT_URL)
            else:
                message = 'Identifiants invalides.'
    return render(request, 'app/homepage.html', context={'form': form, 'message': message})

@login_required
def welcome(request):
    render(request, 'app/base.html')
    return render(request, 'app/welcome.html')

def sign_up(request):
    render(request, 'app/base.html')
    form = forms.SignupForm()
    if request.method == 'POST':
        form = forms.SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
    return render(request, 'app/sign-up.html', context={'form': form})

def logout_user(request):

    logout(request)
    return redirect('homepage')
    