from django.db import models

class Account(models.Model):
	account = models.CharField(max_length=20)
	passwd = models.CharField(max_length=20)
	def __unicode__(self):
		#mysql  give id aoto
		return self.account
	def as_json(self):
		# return dict(account=self.account, passwd=self.passwd)
		return {'account':self.account, 'passwd':self.passwd)
