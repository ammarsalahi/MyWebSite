from accounts.models import Skill
from unfold.admin import ModelAdmin
from django.contrib import admin

@admin.register(Skill)
class SkillAdmin(ModelAdmin):
    list_display=('name','created_at')
    list_filter=('created_at','updated_at')
    search_fields=('name',)