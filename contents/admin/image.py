from django.contrib import admin
from contents.models import Image

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display=('img','created_at')
    list_filter=('created_at','updated_at')
