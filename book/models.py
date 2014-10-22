from django.db import models
from time import time
from django.utils import timezone

def get_upload_file_name(instance, filename):
	return 'uploaded_files/%s_%s'%(str(time()).replace('.','-'), filename)

# Create your Models here.
class Book(models.Model):
	title = models.CharField(max_length=50)
	author = models.CharField(max_length=50)
	description = models.TextField()
	pub_date = models.DateTimeField(default=timezone.now())
	likes = models.IntegerField(default=0)
	thumbnail = models.FileField(upload_to=get_upload_file_name)

	def __unicode__(self):
		return self.title

	def get_absolute_url(self):
		return '/get/%i' % self.id

class Comment(models.Model):
	name = models.CharField(max_length=50)
	body = models.TextField()
	pub_date = models.DateTimeField('date published')
	book = models.ForeignKey(Book)

	def __unicode__(self):
		return self.name