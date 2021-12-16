from django.db import models


class Task(models.Model):
	name = models.CharField(max_length=250, default='None')
	text = models.TextField(default='None')



	def __str__(self):
		return self.name
