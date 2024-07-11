from django.contrib import admin
from contents.models import Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=('name','created_at')
    search_fields=('name',)
    list_filter=('created_at','updated_at')