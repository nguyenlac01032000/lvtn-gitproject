from django.contrib import admin
from .models import Contact

# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'created_date')
    list_display_links = ('name', 'email', 'phone')
    search_fields = ('name', 'email', 'phone' )
    list_per_page = 25

admin.site.register(Contact, ContactAdmin)
