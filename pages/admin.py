from django.contrib import admin
from .models import Team
# Register your models here.

class TeamAdmin(admin.ModelAdmin):
    list_display = ('id', 'First_name', 'Designation', 'Phone','created_date')
    list_display_links = ('id', 'First_name', 'Designation',)
    search_fields = ('id', 'First_name', 'Phone', 'Designation' )
    list_filter = ('Designation',)

admin.site.register(Team, TeamAdmin)

# class MedAdmin(admin.ModelAdmin):
#     list_display = ('id', 'brand', 'model', 'problem', 'created_date', 'is_featured')
#     list_display_links = ('id', 'brand', 'model')
#     search_fields = ('brand', 'model', 'problem' )
#     list_filter = ('brand',)
#     list_editable = ('is_featured',)
#
# admin.site.register(Med, MedAdmin)
