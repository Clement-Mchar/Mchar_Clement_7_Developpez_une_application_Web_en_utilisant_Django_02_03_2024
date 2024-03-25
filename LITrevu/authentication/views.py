from django.conf import settings
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, request
from django.contrib import messages
from .models import User, UserFollow, BlockedUser
from .forms import FollowingForm

from . import forms


# Create your views here.
def sign(request):
    if request.user.is_authenticated:
        return redirect("flux")
    form = forms.LoginForm(request.POST if request.method == "POST" else None)
    if request.method == "POST" and form.is_valid():
        user = authenticate(
            username=form.cleaned_data["username"],
            password=form.cleaned_data["password"],
        )
        if user is not None:
            login(request, user)
            messages.success(request, "bravo chakal")
            return redirect(settings.LOGIN_REDIRECT_URL)
        else:
            messages.error(request, "Identifiants invalides")
    return render(request, "app/sign.html", locals())


@login_required
def welcome():
    return redirect("flux")


def sign_up(request):
    if request.user.is_authenticated:
        return redirect("flux")
    form = forms.SignupForm(request.POST if request.method == "POST" else None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
    return render(request, "app/sign-up.html", context={"form": form})


def logout_user(request):

    logout(request)
    return redirect("sign")


@login_required
def follow_user(request):
    form = FollowingForm(request.POST if request.method == "POST" else None)
    followings = UserFollow.objects.all()
    users_blocked = BlockedUser.objects.filter(blocked_user=request.user)
    blocked_users = BlockedUser.objects.filter(user=request.user)
    if request.method == "POST":
        if form.is_valid():
            for user_blocked in users_blocked:
                if form.cleaned_data["username"] == user_blocked.user.username:
                    return HttpResponse("Utilisateur introuvable")
            for user in blocked_users:
                if form.cleaned_data["username"] == user.blocked_user.username:
                    return HttpResponse("Utilisateur introuvable")
            if form.cleaned_data["username"] != request.user.username:
                UserFollow.objects.create(
                    user=request.user,
                    followed_user=(
                        User.objects.get(username__iexact=form.cleaned_data["username"])
                    ),
                )
                return redirect("followings")
            else:
                return HttpResponse("Vous ne pouvez pas vous ajouter vous-même")
    return render(
        request, "app/followings.html", {"form": form, "followings": followings}
    )


@login_required
def unfollow(request, id):
    following = UserFollow.objects.get(id=id, user=request.user)
    if request.method == "POST":
        following.delete()
        return redirect("followings")


@login_required
def block_user(request, id):
    followed = UserFollow.objects.get(id=id, user=request.user)
    followings = UserFollow.objects.filter(followed_user=request.user)
    if request.method == "POST":
        if followings:
            for following in followings:
                if following.user == followed.followed_user:
                    following.delete()
        followed.delete()
        BlockedUser.objects.create(
            user=request.user,
            blocked_user=User.objects.get(username__iexact=followed.followed_user),
        )
        return redirect("followings")
