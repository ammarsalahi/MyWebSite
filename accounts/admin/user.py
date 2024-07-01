from accounts.models import User
from django.contrib import admin

class UserAdmin(admin.modelAdmin):
    list_display=('username','first_name','last_name')
    