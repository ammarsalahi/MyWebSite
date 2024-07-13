from django.contrib import admin
from contents.models import Technology

@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
    list_display=('name','created_at')
    list_filter=('created_at','updated_at')
    search_fields=('name',)