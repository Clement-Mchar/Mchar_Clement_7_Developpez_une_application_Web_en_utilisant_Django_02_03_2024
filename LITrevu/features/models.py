import uuid
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from django.conf import settings

# Create your models here.


class Ticket(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(
        max_length=128, verbose_name="Titre", null=False, blank=False
    )
    description = models.TextField(
        max_length=2048, blank=True, verbose_name="Description", null=False
    )
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True)
    time_created = models.DateTimeField(auto_now_add=True)


class Review(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    ticket = models.ForeignKey(to=Ticket, on_delete=models.CASCADE)
    headline = models.CharField(
        max_length=128, verbose_name="Titre", null=False, blank=False
    )
    rating = models.PositiveSmallIntegerField(
        # validates that rating must be between 0 and 5
        validators=[MinValueValidator(0), MaxValueValidator(5)],
        verbose_name="Note",
    )
    body = models.TextField(blank=True, verbose_name="Corps du message", null=False)
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    time_created = models.DateTimeField(auto_now_add=True)
