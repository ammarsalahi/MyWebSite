from django.contrib import admin
from contents.models import Post
from unfold.admin import ModelAdmin


@admin.register(Post)
class PostAdmin(ModelAdmin):
    list_display=('title','post_id','created_at')
    search_fields=('title','english_title','post_id')
    list_filter=('created_at','updated_at','is_active')
    readonly_fields=('post_id',)