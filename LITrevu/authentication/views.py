from django.conf import settings
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import User, UserFollow, BlockedUser
from .forms import FollowingForm
from django.db import IntegrityError
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
            messages.success(
                request,
                f"Vous êtes connecté en tant que {request.user.username}.",
            )
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
    if request.method == "POST":
        if form.is_valid():
            try:
                user_to_follow = User.objects.get(
                    username__iexact=form.cleaned_data["username"]
                )
            except User.DoesNotExist:
                messages.error(request, "Cet utilisateur n'existe pas")
                print(request.user.id)
                return redirect("followings")
            if BlockedUser.objects.filter(
                user=request.user, blocked_user=user_to_follow
            ).exists():
                messages.error(request, "Utilisateur introuvable")
                return redirect("followings")
            if BlockedUser.objects.filter(
                user=user_to_follow, blocked_user=request.user
            ).exists():
                messages.error(request, "Utilisateur introuvable")
                return redirect("followings")
            if user_to_follow.id == request.user.id:
                messages.error(request, "Vous ne pouvez pas vous abonner à vous même.")
                return redirect("followings")
            try:
                UserFollow.objects.create(
                    user=request.user, followed_user=user_to_follow
                )
            except IntegrityError:
                messages.error(request, "Vous suivez déjà cet utilisateur.")
                return redirect("followings")
        return redirect("followings")


@login_required
def unfollow(request, id):
    following = UserFollow.objects.get(id=id, user=request.user)
    if request.method == "POST":
        following.delete()
        return redirect("followings")


@login_required
def delete_follow(request, id):
    following = UserFollow.objects.get(id=id, followed_user=request.user)
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
        if followed.followed_user != request.user:
            followed.delete()
            BlockedUser.objects.create(
                user=request.user,
                blocked_user=User.objects.get(username__iexact=followed.followed_user),
            )
        return redirect("followings")
