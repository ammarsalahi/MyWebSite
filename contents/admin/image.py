from django.contrib import admin
from contents.models import Image
from unfold.admin import ModelAdmin

@admin.register(Image)
class ImageAdmin(ModelAdmin):
    list_display=('img','created_at')
    list_filter=('created_at','updated_at')
