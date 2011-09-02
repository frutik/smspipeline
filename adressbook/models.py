from django.db import models
from django.contrib.auth.models import User

class AdressBook(models.Model):
    title = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    owner = models.ForeignKey(User)

    def __unicode__(self):
        return self.title
