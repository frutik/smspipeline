from django.db import models
from django.contrib.auth.models import User

class MessageTemplate(models.Model):
    title = models.CharField(max_length=255)
    regexp = models.CharField(max_length=255, blank=True)
    template = models.TextField(blank=True)
    owner = models.ForeignKey(User, blank=False, null=False)

    def __unicode__(self):
        return self.title
