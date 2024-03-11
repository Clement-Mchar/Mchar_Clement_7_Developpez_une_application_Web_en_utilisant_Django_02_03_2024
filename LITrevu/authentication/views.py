from django.conf import settings
from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.http import HttpResponse, request

from . import forms


# Create your views here.
def homepage(request):
    render(request, 'app/base.html')
    return render(request, 'app/homepage.html')

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
            # auto-login user
            login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)
    return render(request, 'app/sign-up.html', context={'form': form})
