__author__ = 'frutik'

from django import forms
from message_template.models import MessageTemplate

class MessageTemplateForm(forms.ModelForm):
    error_css_class = 'clearfix error'
    class Meta:
        model = MessageTemplate
        exclude = ('owner',)
