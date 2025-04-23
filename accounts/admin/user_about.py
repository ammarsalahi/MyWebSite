from django.contrib import admin
from accounts.models import UserAbout
from unfold.admin import ModelAdmin


@admin.register(UserAbout)
class UserAboutAdmin(ModelAdmin):
    list_display=('user','created_at')
    list_filter=('created_at','updated_at')
    search_fields=('skill','university_name','university_web')