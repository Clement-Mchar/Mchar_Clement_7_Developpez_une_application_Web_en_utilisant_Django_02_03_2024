from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import TicketForm, ReviewForm, ReviewResponse

# Create your views here.
@login_required
def flux(request):
    return render(request, 'app/flux.html')

@login_required
def create_review(request):
    form = ReviewForm()
    return render(request, 'app/create-review.html', {'form':form})

@login_required
def create_ticket(request):
    form = TicketForm()
    return render(request, 'app/create-ticket.html', {'form':form})

@login_required
def user_posts(request):
    return render(request, 'app/user-posts.html')
