from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.utils.safestring import mark_safe
from django.utils import timezone
# Create your models here.

class userSearch(models.Model):
	login = models.CharField(max_length=120)
	id = models.IntegerField(unique=True,primary_key=True)
	avatar_url = models.TextField()
	name = models.TextField(null=True)
	email = models.EmailField(blank=True, null=True)
	public_repos = models.IntegerField()
	followers = models.IntegerField()
	following =models.IntegerField()
	publish = models.DateField(auto_now=False, auto_now_add=False, default=timezone.now().date())
	timestamp = models.DateField(auto_now=False, auto_now_add=True)
	updatedtime = models.DateField(auto_now=True, auto_now_add=False)


	def __unicode__(self):
		return self.login

	def image_tag(self):
		return mark_safe('<img src='+self.avatar_url+' width="30" height="30" />')

	image_tag.short_description = 'Image'

class queryReport(models.Model):
	requested = models.TextField()
	timestamp = models.DateField(auto_now=False, auto_now_add=True)


