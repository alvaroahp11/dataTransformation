from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as AbstractUserAdmin
from .models import User

# Register your models here.

@admin.register(User)
class UserAdmin(AbstractUserAdmin):
    pass
