from django.contrib import admin
from contents.models import Category
from unfold.admin import ModelAdmin


@admin.register(Category)
class CategoryAdmin(ModelAdmin):
    list_display=('name','created_at')
    search_fields=('name',)
    list_filter=('created_at','updated_at')