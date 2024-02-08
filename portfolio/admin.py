from django.contrib import admin
from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name', 'email', 'message', 'created_at')
    ordering = ('-created_at',)

admin.site.register(Contact, ContactAdmin)
