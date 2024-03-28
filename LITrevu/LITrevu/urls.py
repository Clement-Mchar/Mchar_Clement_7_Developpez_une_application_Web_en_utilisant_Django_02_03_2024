"""
URL configuration for LITrevu project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from authentication import views
from features import views as features_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("sign", views.sign, name="sign"),
    path("sign-up", views.sign_up, name="sign-up"),
    path("welcome", views.welcome, name="welcome"),
    path("logout/", views.logout_user, name="logout"),
    path("flux", features_views.flux, name="flux"),
    path(
        "posts/create_review",
        features_views.create_review,
        name="create_review",
    ),
    path(
        "posts/create_ticket",
        features_views.create_ticket,
        name="create_ticket",
    ),
    path("posts/", features_views.user_posts, name="user_posts"),
    path("followings", features_views.followings, name="followings"),
    path("follow_user", views.follow_user, name="follow_user"),
    path("followings#unfollow", views.follow_user, name="unfollow_modal"),
    path("followings#block-user", views.follow_user, name="block_modal"),
    path(
        "followings#delete-follow",
        views.follow_user,
        name="delete_follow_modal",
    ),
    path("ticket/<id>/", features_views.ticket, name="ticket"),
    path("ticket/<id>/#modal-ticket", features_views.ticket, name="ticket_modal"),
    path(
        "ticket_response/<id>",
        features_views.ticket_response,
        name="ticket_response",
    ),
    path("review/<id>/#modal-review", features_views.review, name="review"),
    path("review/<id>/", features_views.review, name="review_modal"),
    path("edit_ticket/<id>/", features_views.update_ticket, name="update_ticket"),
    path("edit_review/<id>/", features_views.update_review, name="update_review"),
    path(
        "delete_ticket/<id>",
        features_views.delete_ticket,
        name="delete_ticket",
    ),
    path(
        "delete_review/<id>",
        features_views.delete_review,
        name="delete_review",
    ),
    path("unfollow/<id>", views.unfollow, name="unfollow"),
    path("delete_follow/<id>", views.delete_follow, name="delete_follow"),
    path("block/<id>", views.block_user, name="block_user"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
