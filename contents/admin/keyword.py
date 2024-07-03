from django.contrib import admin

class KeywordAdmin(admin.ModelAdmin):
    list_display=('name','created_at')
    search_fields=('name',)
    list_filter=('created_at',)