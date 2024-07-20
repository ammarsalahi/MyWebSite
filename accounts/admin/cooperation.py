from django.contrib import admin
from accounts.models import Cooperation

@admin.register(Cooperation)
class CooperationAdmin(admin.ModelAdmin):
    list_display=('name','types','created_at')
    list_filter=('created_at','updated_at')
    search_fields=('name','types','email','phone_number')