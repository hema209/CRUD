from django.db import models

class Student(models.Model):
	name = models.CharField(max_length=100)
	s_id = models.IntegerField()
	branch = models.CharField(max_length=100) 

	def __str__(self):
		return self.name