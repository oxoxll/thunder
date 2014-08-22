from django.db import models

class Account(models.Model):
	account = models.CharField(max_length=20)
	passwd = models.CharField(max_length=20)
	def __unicode__(self):
		#mysql  give id aoto
		return self.account