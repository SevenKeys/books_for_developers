from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

import logging
logr = logging.getLogger(__name__)

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    programmer = models.BooleanField(default=False)
    speciality = models.CharField(max_length=50)
    
    
User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])

@receiver(post_save, sender=User)
def make_sure_user_profile_is_added_on_user_created(sender, **kargs):
	if kargs.get('created',False):
		up = UserProfile.objects.create(user=kargs.get('instance'))
		logr.debug('UserProfile created: %s' % up)