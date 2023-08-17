from django.db import models

class Description(models.Model):
	description = models.CharField(max_length=100)


class Course(models.Model):
	name = models.CharField(max_length=50)
	desc = models.OneToOneField(Description, on_delete=models.CASCADE, primary_key=True)
	created_at = models.DateTimeField(auto_now_add=True)

