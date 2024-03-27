import uuid
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.db.models import UniqueConstraint
from django.conf import settings
from django.db import models
from .managers import UserManager

# Create your models here.


class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(
        max_length=40, unique=True, verbose_name="Nom d'utilisateur"
    )
    is_active = models.BooleanField(("active"), default=True)
    is_staff = models.BooleanField(("staff"), default=False)
    is_superuser = models.BooleanField(("superuser"), default=False)
    USERNAME_FIELD = "username"

    objects = UserManager()

    class Meta:
        db_table = "auth_user"


class UserFollow(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="following",
    )
    followed_user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="followed_by",
    )

    class Meta:
        # ensures we don't get multiple UserFollows instances
        # for unique user-user_followed pairs
        constraints = [
            UniqueConstraint(
                name="unique_follow", fields={"user", "followed_user"}
            )
        ]


class BlockedUser(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="blocker",
    )
    blocked_user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="blocked_user",
    )

    class Meta:
        # ensures we don't get multiple UserFollows instances
        # for unique user-user_followed pairs
        unique_together = (
            "user",
            "blocked_user",
        )
