from django.contrib import admin
from contents.models import Project
from unfold.admin import ModelAdmin

@admin.register(Project)
class ProjectAdmin(ModelAdmin):
    list_display=('title','project_id','created_at')
    search_fields=('title','project_id')
    list_filter=('created_at','updated_at')
    readonly_fields=('project_id',)