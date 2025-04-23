from django.contrib import admin
from contents.models import ChoiceContent
from unfold.admin import ModelAdmin


@admin.register(ChoiceContent)
class ChoiceContentAdmin(ModelAdmin):
    list_display=('selected_post','created_at')
    search_fields=('selected_post',)
    list_filter=('created_at','updated_at')