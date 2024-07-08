from django.contrib import admin
from contents.models import Keyword

@admin.register(Keyword)
class KeywordAdmin(admin.ModelAdmin):
    list_display=('name','created_at')
    search_fields=('name',)
    list_filter=('created_at',)