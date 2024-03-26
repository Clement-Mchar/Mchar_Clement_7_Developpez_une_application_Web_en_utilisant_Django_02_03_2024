from django.contrib import admin
from .models import User, UserFollow, BlockedUser

# Register your models here.

admin.site.register(User)
admin.site.register(UserFollow)
admin.site.register(BlockedUser)
