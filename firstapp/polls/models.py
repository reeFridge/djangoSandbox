
import datetime

from django.utils import timezone
from django.db import models

class Question(models.Model):
	question_text = models.CharField(max_length = 200)
	pub_date = models.DateTimeField('date published')
	def __str__(self):
		return self.question_text
	def was_pub_rcntly(self):
		now = timezone.now()
		return now - datetime.timedelta(days=1) <= self.pub_date <= now
	was_pub_rcntly.admin_order_field = 'pub_date'
	was_pub_rcntly.boolean = True
	was_pub_rcntly.short_description = 'Published recently?'
	
class Choice(models.Model):
	question = models.ForeignKey(Question)
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)
	def __str__(self):
		return self.choice_text
