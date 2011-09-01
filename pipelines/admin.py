from pipelines.models import AdressBook
from pipelines.models import Pipeline, MessageTemplate
from django.contrib import admin

class AdressBookAdmin(admin.ModelAdmin):
    pass
    
class PipelineAdmin(admin.ModelAdmin):
    pass

class MessageTemplateAdmin(admin.ModelAdmin):
    pass
    
admin.site.register(AdressBook, AdressBookAdmin)
admin.site.register(Pipeline, PipelineAdmin)
admin.site.register(MessageTemplate, MessageTemplateAdmin)
