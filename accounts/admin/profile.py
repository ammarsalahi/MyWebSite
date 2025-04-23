from django.contrib import admin
from accounts.models import Profile
from unfold.admin import ModelAdmin


@admin.register(Profile)
class ProfileAdmin(ModelAdmin):
    list_display=('user','created_at')
    list_filter=('created_at','updated_at')