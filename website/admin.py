from django.contrib import admin

from .models import Publication

class PublicationAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'date')
    list_filter = ['date']

admin.site.register(Publication, PublicationAdmin)
