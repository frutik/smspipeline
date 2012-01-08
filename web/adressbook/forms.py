__author__ = 'frutik'

from django import forms
from adressbook.models import AdressBook

class AdressBookForm(forms.ModelForm):
    #error_css_class = 'clearfix error'
    class Meta:
        model = AdressBook
        exclude = ('owner',)
