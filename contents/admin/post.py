from django.contrib import admin

class PostAdmin(admin.ModelAdmin):
    list_display=('title','post_id','created_at')
    search_fields=('title','post_id')
    list_filter=('created_at',)