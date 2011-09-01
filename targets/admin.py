from targets.models import MailTarget, TwitterTarget
from django.contrib import admin

class MailTargetAdmin(admin.ModelAdmin):
    list_display_links = list_display = ('title', 'enabled')
    list_filter = ('enabled',)

class TwitterTargetAdmin(MailTargetAdmin):
    pass
    
admin.site.register(MailTarget, MailTargetAdmin)
admin.site.register(TwitterTarget, TwitterTargetAdmin)
