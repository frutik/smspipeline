from targets.models import MailTarget, TwitterTarget
from django.contrib import admin

class MailTargetAdmin(admin.ModelAdmin):
    pass

class TwitterTargetAdmin(admin.ModelAdmin):
    pass
    
admin.site.register(MailTarget, MailTargetAdmin)
admin.site.register(TwitterTarget, TwitterTargetAdmin)
