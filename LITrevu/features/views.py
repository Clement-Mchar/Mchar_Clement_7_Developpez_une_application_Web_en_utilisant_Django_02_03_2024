from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import CharField, Value
from itertools import chain
from .forms import TicketForm, ReviewForm, ReviewResponse
from .models import Ticket, Review

# Create your views here.
@login_required
def flux(request):
    return render(request, 'app/flux.html')

@login_required
def create_review(request):
    form2 = ReviewForm(request.POST if request.method == 'POST' else None)
    form1 = TicketForm(request.POST if request.method == 'POST' else None)
    if form1.is_valid() and form2.is_valid():
        ticket = form1.save(commit=False)
        review = form2.save(commit=False)
        ticket.user = request.user
        ticket.save()
        review.ticket = ticket
        review.user = request.user
        review.save()
    return render(request, 'app/create-review.html', context={'form1':form1, 'form2':form2})

@login_required
def create_ticket(request):
    form = TicketForm(request.POST if request.method == 'POST' else None)
    if form.is_valid():
        ticket = form.save(commit=False)
        ticket.user = request.user
        ticket.save()
        return redirect('flux')
    return render(request, 'app/create-ticket.html', {'form':form})

@login_required
def user_posts(request):
    tickets = Ticket.objects.filter(user=request.user)
    reviews = Review.objects.filter(user=request.user)

    reviews = reviews.annotate(content_type=Value('REVIEW', CharField()))
    tickets = tickets.annotate(content_type=Value('TICKET', CharField()))

    posts = sorted(
    chain(reviews, tickets),
        key=lambda post: post.time_created,
        reverse=True
    )

    return render(request, 'app/user-posts.html', context={'posts':posts})


@login_required
def followings(request):
    return render(request, 'app/followings.html')

@login_required
def ticket(request, id):
    ticket = Ticket.objects.get(id=id)
    return render(request, 'app/selected-ticket.html', {'post':ticket})
