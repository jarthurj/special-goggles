from django.db import models
from django.core.exceptions import ValidationError
import re
def validateLenGreaterThanTwo(value):
	if len(value)<3:
		raise ValidationError(
			"{} must longer than 2".format(value)
			)

def validateLenGreaterThanSeven(value):
	if len(value)<3:
		raise ValidationError(
			"Password must be 8 characters or longer"
			)

def validateEmail(value):
	regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
	if not re.fullmatch(regex, value):
		raise ValidationError(
			"Please enter a valid email address"
			)
class User(models.Model):
	first_name = models.CharField(max_length=100, validators=[validateLenGreaterThanTwo])
	last_name = models.CharField(max_length=100, validators=[validateLenGreaterThanTwo])
	username = models.CharField(max_length=100, validators=[validateLenGreaterThanTwo])
	password = models.CharField(max_length=100, validators=[validateLenGreaterThanSeven])
	email = models.CharField(max_length=100, validators=[validateEmail])
