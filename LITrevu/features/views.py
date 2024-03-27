from django.shortcuts import render, redirect
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.db.models import CharField, Value
from itertools import chain
from .forms import TicketForm, ReviewForm
from .models import Ticket, Review
from authentication.models import UserFollow
from authentication.forms import FollowingForm

# Create your views here.


@login_required
def create_review(request):
    form2 = ReviewForm(request.POST if request.method == "POST" else None)
    form1 = TicketForm(
        request.POST if request.method == "POST" else None,
        request.FILES if request.method == "POST" else None,
    )
    if request.method == "POST":
        if form1.is_valid() and form2.is_valid():
            ticket = form1.save(commit=False)
            review = form2.save(commit=False)
            ticket.user = request.user
            ticket.save()
            review.ticket = ticket
            review.user = request.user
            review.save()
            return redirect("user_posts")
    return render(
        request,
        "app/create-review.html",
        context={"form1": form1, "form2": form2},
    )


@login_required
def ticket_response(request, id):
    ticket = Ticket.objects.get(id=id)
    form = ReviewForm(
        request.POST if request.method == "POST" else None,
        request.FILES if request.method == "POST" else None,
    )
    if request.method == "POST":
        if form.is_valid():
            review = form.save(commit=False)
            review.ticket = ticket
            review.user = request.user
            review.save()
            return redirect("user_posts")
    return render(
        request,
        "app/ticket_response.html",
        context={"form": form, "ticket": ticket},
    )


@login_required
def create_ticket(request):
    form = TicketForm(
        request.POST if request.method == "POST" else None,
        request.FILES if request.method == "POST" else None,
    )
    if request.method == "POST":
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            return redirect("user_posts")
    return render(request, "app/create-ticket.html", {"form": form})


@login_required
def user_posts(request):
    tickets = Ticket.objects.filter(user=request.user)
    reviews = Review.objects.filter(user=request.user)

    reviews = reviews.annotate(content_type=Value("REVIEW", CharField()))
    tickets = tickets.annotate(content_type=Value("TICKET", CharField()))
    posts = sorted(
        chain(reviews, tickets),
        key=lambda post: post.time_created,
        reverse=True,
    )

    return render(request, "app/user-posts.html", context={"posts": posts})


@login_required
def flux(request):
    followings = UserFollow.objects.filter(user=request.user)
    if followings:
        tickets = Ticket.objects.exclude(user=request.user)
        reviews = Review.objects.exclude(user=request.user)
        reviews = reviews.annotate(content_type=Value("REVIEW", CharField()))
        tickets = tickets.annotate(content_type=Value("TICKET", CharField()))
        user_tickets = Ticket.objects.filter(user=request.user)
        user_reviews = Review.objects.filter(user=request.user)
        user_reviews = user_reviews.annotate(
            content_type=Value("REVIEW", CharField())
        )
        user_tickets = user_tickets.annotate(
            content_type=Value("TICKET", CharField())
        )
        all_reviews = sorted(
            chain(reviews, user_reviews),
            key=lambda post: post.time_created,
            reverse=True,
        )
        all_tickets = sorted(
            chain(tickets, user_tickets),
            key=lambda post: post.time_created,
            reverse=True,
        )
        posts = sorted(
            chain(all_reviews, all_tickets),
            key=lambda post: post.time_created,
            reverse=True,
        )
        return render(
            request,
            "app/flux.html",
            context={"posts": posts, "followings": followings},
        )
    else:
        return render(request, "app/flux.html")


@login_required
def followings(request):
    form = FollowingForm(request.POST if request.method == "POST" else None)
    return render(request, "app/followings.html", {"form": form})


@login_required
def ticket(request, id):
    ticket = Ticket.objects.get(id=id)
    return render(request, "app/selected-ticket.html", {"post": ticket})


@login_required
def review(request, id):
    review = Review.objects.get(id=id)
    return render(request, "app/selected-review.html", {"post": review})


@login_required
def update_ticket(request, id):
    ticket = Ticket.objects.get(id=id, user=request.user)
    ticket_form = TicketForm(
        request.POST if request.method == "POST" else None,
        request.FILES if request.FILES else None,
        instance=ticket,
    )
    if ticket_form.is_valid():
        ticket.time_created = datetime.now()
        ticket_form.save()
        return redirect("user_posts")
    return render(request, "app/update-post.html", {"form": ticket_form})


@login_required
def update_review(request, id):
    review = Review.objects.get(id=id, user=request.user)
    review_form = ReviewForm(
        request.POST if request.method == "POST" else None,
        request.FILES if request.FILES else None,
        instance=review,
    )
    return render(request, "app/update-post.html", {"form": review_form})


@login_required
def delete_ticket(request, id):
    ticket = Ticket.objects.get(id=id, user=request.user)
    if request.method == "POST":
        ticket.delete()
        return redirect("user_posts")


@login_required
def delete_review(request, id):
    review = Review.objects.get(id=id, user=request.user)
    if request.method == "POST":
        review.delete()
        return redirect("user_posts")
