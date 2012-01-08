from django.contrib import admin
from pipelines.models import Pipeline

class PipelineAdmin(admin.ModelAdmin):
    list_display_links = list_display = ('title', 'owner')

admin.site.register(Pipeline, PipelineAdmin)
