from django.db import models
from django.contrib.auth.models import User

class MessageTemplate(models.Model):
    title = models.CharField(max_length=255)
    regexp = models.CharField(max_length=255, blank=True)
    template = models.TextField(blank=True)
    owner = models.ForeignKey(User, blank=False, null=False)

    grid_columns = [
        {'key':'title', 'label':'Title'},
    ]

    # TODO DRY
    def get_attribute_by_name(self, name):
        return self.__dict__[name]

    def __unicode__(self):
        return self.title
