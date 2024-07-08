from django.contrib import admin
from contents.models import Comment

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display=('email','is_verified','created_at')
    search_fields=('text','email')
    list_filter=('created_at',)