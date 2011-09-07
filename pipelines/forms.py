__author__ = 'frutik'

from django import forms
from pipelines.models import Pipeline

class PipelineForm(forms.ModelForm):
    error_css_class = 'clearfix error'
    class Meta:
        model = Pipeline
        exclude = ('owner',)
