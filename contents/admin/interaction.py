from django.contrib import admin

class InteractionAdmin(admin.ModelAdmin):
    list_display=('action','created_at')
    search_fields=('action',)
    list_filter=('created_at',)