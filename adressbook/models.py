from django.db import models
from django.contrib.auth.models import User
from settings import MEDIUM_COLUMN_WIDTH

class AdressBook(models.Model):
    title = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    owner = models.ForeignKey(User)

    grid_columns = [
        {'key':'title', 'label':'Title'},
        {'key':'phone_number', 'label':'Phone', 'width':MEDIUM_COLUMN_WIDTH}
    ]

    def get_attribute_by_name(self, name):
        return self.__dict__[name]

    def __unicode__(self):
        return self.title

