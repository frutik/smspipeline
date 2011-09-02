from django.db import models
from django.contrib.auth.models import User

from targets.models import Target
from message_template.models import MessageTemplate
from adressbook.models import AdressBook

class Pipeline(models.Model):
    title = models.CharField(max_length=255)
    
    #probably this model is wrong place for these options??
    pin = models.CharField(max_length=255) 
    command = models.CharField(max_length=255)
    senders = models.ManyToManyField(AdressBook) 

    message_template = models.ForeignKey(MessageTemplate)

    targets = models.ManyToManyField(Target) 

    enabled = models.BooleanField()
    owner = models.ForeignKey(User)

    def __unicode__(self):
        return self.title

    @staticmethod
    def getSMS(sender, sms):
	pin, command, message_txt = sms.split(' ', 2)

	pipeline = Pipeline.objects.get(pin=pin, senders__phone_number=sender, command=command, enabled=True)

	return pipeline, Message(message_txt, pipeline.message_template)

class Message(object):
    
    def __init__(self, txt, template):
	self.txt = txt
	self.template = template
	
    def is_parsable(self):
	return bool(self.template)

    def get(self):
	if not self.template.regexp:
    	    return self.txt

	return 'something else'