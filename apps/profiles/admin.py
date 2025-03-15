from django.contrib import admin
from .models import User, Profile


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "gender", "is_deleted")
    list_filter = ("gender", "is_deleted")
    search_fields = ("username", "email")


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "is_active")
    list_filter = ("is_active",)
