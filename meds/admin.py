from django.contrib import admin
from .models import Med
# Register your models here.

class MedAdmin(admin.ModelAdmin):
    list_display = ('id', 'brand', 'model', 'problem', 'created_date', 'is_featured')
    list_display_links = ('id', 'brand', 'model')
    search_fields = ('brand', 'model', 'problem' )
    list_filter = ('brand',)
    list_editable = ('is_featured',)

admin.site.register(Med, MedAdmin)
