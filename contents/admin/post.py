from django.contrib import admin
from contents.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display=('title','post_id','created_at')
    search_fields=('title','post_id')
    list_filter=('created_at','updated_at','is_active')
    readonly_fields=('post_id',)