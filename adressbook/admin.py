from django.contrib import admin
from adressbook.models import AdressBook

class AdressBookAdmin(admin.ModelAdmin):
    list_display_links = list_display = ('title', 'owner')

admin.site.register(AdressBook, AdressBookAdmin)
