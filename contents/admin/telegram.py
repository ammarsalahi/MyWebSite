from django.contrib import admin
from contents.models import TelegramChannel
from unfold.admin import ModelAdmin

@admin.register(TelegramChannel)
class TelegramAdmin(ModelAdmin):
    list_display=('channel_id','is_selected','type_channel')
    search_fields=('title',)
    list_filter=('created_at','updated_at',"is_selected","type_channel")
    # readonly_fields=('project_id',)