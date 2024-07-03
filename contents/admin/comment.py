from django.contrib import admin

class CommentAdmin(admin.ModelAdmin):
    list_display=('user','created_at')
    search_fields=('text',)
    list_filter=('created_at',)