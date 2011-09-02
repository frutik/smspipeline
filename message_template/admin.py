from django.contrib import admin
from message_template.models import MessageTemplate

class MessageTemplateAdmin(admin.ModelAdmin):
    list_display_links = list_display = ('title', 'owner')

admin.site.register(MessageTemplate, MessageTemplateAdmin)
