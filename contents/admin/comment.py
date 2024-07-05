from django.contrib import admin


class CommentAdmin(admin.ModelAdmin):
    list_display=('email','is_verified','created_at')
    search_fields=('text','email')
    list_filter=('created_at',)