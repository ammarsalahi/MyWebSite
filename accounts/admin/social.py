from django.contrib import admin
from accounts.models import Social

@admin.register(Social)
class SocialAdmin(admin.ModelAdmin):
    list_display=('name','link','created_at')
    list_filter=('created_at','updated_at')
    search_fields=('name','link')