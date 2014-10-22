from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Notification(models.Model):
	title = models.CharField(max_length=50)
	message = models.TextField()
	viewed = models.BooleanField(default=False)
	user = models.ForeignKey(User)

@receiver(post_save, sender=User)
def create_welcome_message(sender, **kargs):
	if kargs.get('created', False):
		Notification.objects.create(user=kargs.get('instance'),
			title='Welcome to our site!',
			message='We are glad you join us!')