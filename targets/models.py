from django.db import models

TWITTER='twitter'
MAIL='mail'

TARGET_CHOICES = (
    (TWITTER, TWITTER),
    (MAIL, MAIL),
)

class Target(models.Model):
    title = models.CharField(max_length=255)
    kind = models.CharField(max_length=255, editable=False, choices=TARGET_CHOICES)

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.kind:
            self.kind = self.exact_type

        super(Target,self).save(*args, **kwargs)

class MailTarget(Target):

    exact_type = MAIL
    email = models.EmailField(max_length=255)

class TwitterTarget(Target):

    exact_type = TWITTER
    access_key = models.CharField(max_length=255)
    access_secret = models.CharField(max_length=255)

class TargetRunner(object):

    def __init__(self, target_options):
	pass
	
    def send(self,message):

	print self, message

class TwitterTargetRunner(TargetRunner):

    def __init__(self, target_options):

	self.ACCESS_KEY = target_options.twittertarget.access_key
	self.ACCESS_SECRET = target_options.twittertarget.access_secret

    def send(self,message):

	print self, message

	import tweepy, targets.credentials
	
	auth = tweepy.OAuthHandler(targets.credentials.CONSUMER_KEY, targets.credentials.CONSUMER_SECRET)
	
	auth.set_access_token(self.ACCESS_KEY, self.ACCESS_SECRET)
	api = tweepy.API(auth)
	api.update_status(message)	

class MailTargetRunner(TargetRunner):
    pass
	
class TargetRunnerFactory:

    RUNNERS = {
	TWITTER: TwitterTargetRunner, 
	MAIL: MailTargetRunner
    }
        
    @staticmethod
    def get_runner(target_options):
	return TargetRunnerFactory.RUNNERS[target_options.kind](target_options)
