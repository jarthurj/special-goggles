from django.db import models

class UserManager(models.Manager):
	def reg_validator(self, postData):
		errors = {}
		if len(postData['first_name'])<2:
			errors['first_name'] = "First name must be 2 characters or longer."
		if len(postData['last_name'])<2:
			errors['last_name'] = "Last name must be 2 characters or longer."
		for c in postData['first_name']:
			if ord(c.lower()) < 97 or ord(c.lower())>122:
				errors['alphabet'] = "Names can only contain letters"
		if 'alphabet' not in errors:
			for c in postData['last_name']:
				if ord(c.lower()) < 97 or ord(c.lower())>122:
					errors['alphabet'] = "Names can only contain letters"
		return errors
class User(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	email = models.EmailField()
	pw = models.CharField(max_length=50)
	objects = UserManager()