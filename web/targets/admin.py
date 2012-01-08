from targets.models import MailTarget, TwitterTarget
from django.contrib import admin

class MailTargetAdmin(admin.ModelAdmin):
    list_display_links = list_display = ('title', 'enabled')
    list_filter = ('enabled',)

    actions = ['disable_selected', 'enable_selected']

    
    def disable_selected(self, request, queryset):
	self.set_enabled(request, queryset, enabled=False)

    def enable_selected(self, request, queryset):
	self.set_enabled(request, queryset, enabled=True)

    def set_enabled(self, request, queryset, enabled):
	for obj in queryset:
            obj.enabled = enabled
            obj.save()
            
        self.message_user(request, "%s targets were successfully updated" % len(queryset))

    enable_selected.short_description = 'Enable selected targets'
    disable_selected.short_description = 'Disable selected targets'

class TwitterTargetAdmin(MailTargetAdmin):
    pass
    
admin.site.register(MailTarget, MailTargetAdmin)
admin.site.register(TwitterTarget, TwitterTargetAdmin)
