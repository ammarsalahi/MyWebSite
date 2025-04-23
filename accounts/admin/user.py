from accounts.models import User
from django.contrib import admin
from unfold.admin import ModelAdmin


@admin.register(User)
class UserAdmin(ModelAdmin):
    list_display=('username','first_name','last_name','is_active')
    search_fields=('username','first_name','last_name')
    list_filter=('is_superuser','is_active')
    

    