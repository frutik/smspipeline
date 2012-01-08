from django import forms
from targets.models import MailTarget, TwitterTarget

class MailTargetForm(forms.ModelForm):
    class Meta:
        model = MailTarget
        exclude = ('owner',)

class TwitterTargetForm(forms.ModelForm):
    class Meta:
        model = TwitterTarget
