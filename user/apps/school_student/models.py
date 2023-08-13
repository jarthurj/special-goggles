from django.db import models

class School(models.Model):
	name = models.CharField(max_length=255)
	city = models.CharField(max_length=255)
	state = models.CharField(max_length=255)
	desc = models.CharField(max_length=255)

class Student(models.Model):
	school = models.ForeignKey(School, related_name='students', on_delete=models.CASCADE)
	fist_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)