#from django.dispatch import receiver
from registration.signals import user_activated
from pipeline.models import MessageTemplate

#@receiver(user_activated, sender=MyModel)
#def my_handler(sender, **kwargs):

def login_on_activation(sender, user, request, **kwargs):
    user.backend='django.contrib.auth.backends.ModelBackend' 
    login(request,user)

def create_stuff_on_activation(sender, user, request, **kwargs):
    template = MessageTemplate()
    template.owner = user
    template.title = u'simple template'
#    regexp
#    template
    template.save()

user_activated.connect(login_on_activation)
user_activated.connect(create_stuff_on_activation)
