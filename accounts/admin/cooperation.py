from accounts.models import Cooperation
from unfold.admin import ModelAdmin
from django.contrib import admin


@admin.register(Cooperation)
class CooperationAdmin(ModelAdmin):
    list_display=('name','types','created_at')
    list_filter=('created_at','updated_at')
    search_fields=('name','types','email','phone_number')