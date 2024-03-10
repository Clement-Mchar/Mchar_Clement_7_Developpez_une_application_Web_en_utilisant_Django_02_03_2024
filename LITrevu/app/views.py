from django.shortcuts import render
from django.http import HttpResponse, request


# Create your views here.
def homepage(request):
    render(request, 'app/base.html')
    return render(request, 'app/homepage.html')

def sign_up(request):
    render(request, 'app/base.html')
    return render(request, 'app/sign-up.html')