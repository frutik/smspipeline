from django.db import models
from django.contrib.auth.models import User

PROTECH='protech'
DIRECTORY='directory'

TARGET_CHOICES = (
    (DIRECTORY, DIRECTORY),
    (PROTECH, PROTECH),
)

class ServicePoller(models.Model):
    title = models.CharField(max_length=255)
    kind = models.CharField(max_length=255, editable=False, choices=TARGET_CHOICES)
    enabled = models.BooleanField()
    owner = models.ForeignKey(User)

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.kind:
            self.kind = self.exact_type

        super(Target,self).save(*args, **kwargs)

class ProtechServicePoller(ServicePoller):

    exact_type = PROTECH

    uri = models.CharField(max_length=255)
    login = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
