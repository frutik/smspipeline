__author__ = 'frutik'

from django import forms
from adressbook.models import AdressBook

class AdressBookForm(forms.ModelForm):
    class Meta:
        model = AdressBook
        exclude = ('owner',)
