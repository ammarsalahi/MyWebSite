from django.contrib import admin
from contents.models import Keyword
from unfold.admin import ModelAdmin

@admin.register(Keyword)
class KeywordAdmin(ModelAdmin):
    list_display=('name','created_at')
    search_fields=('name',)
    list_filter=('created_at',)