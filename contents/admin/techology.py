from django.contrib import admin
from contents.models import Technology
from unfold.admin import ModelAdmin

@admin.register(Technology)
class TechnologyAdmin(ModelAdmin):
    list_display=('name','created_at')
    list_filter=('created_at','updated_at')
    search_fields=('name',)