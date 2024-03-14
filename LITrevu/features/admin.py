from django.contrib import admin
from .models import Review, Ticket, UserFollow

# Register your models here.
admin.site.register(Review)
admin.site.register(Ticket)
admin.site.register(UserFollow)