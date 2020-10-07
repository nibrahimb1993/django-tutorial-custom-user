from django.contrib import admin

# Register your models here.
from profiles.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        "username",
        "display_name"
    )
