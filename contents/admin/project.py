from django.contrib import admin
from contents.models import Project

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display=('title','project_id','created_at')
    search_fields=('title','project_id')
    list_filter=('created_at','updated_at')