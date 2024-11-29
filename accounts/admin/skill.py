from django.contrib import admin
from accounts.models import Skill

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display=('name','created_at')
    list_filter=('created_at','updated_at')
    search_fields=('name',)