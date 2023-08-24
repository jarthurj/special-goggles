from django.db import models
import re
import datetime
import pytz
class UserManager(models.Manager):
	def birthday_valid(birthday):
		today = datetime.datetime.now()
		verify_year = datetime.datetime(year=today.year-13,month=today.month, day=today.day)
		if (birthday.year <=verify_year.year and
			birthday.month <= verify_year.month and
			birthday.day <= verify_year.day):
			return True
		else:
			return False
	def reg_validator(self, postData):
		errors = {}
		regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
		if len(postData['first_name'])<2:
			errors['first_name'] = "First name must be 2 characters or longer."
		if len(postData['last_name'])<2:
			errors['last_name'] = "Last name must be 2 characters or longer."
		for c in postData['first_name']:
			if ord(c.lower()) < 97 or ord(c.lower())>122:
				errors['alphabet'] = "Names can only contain letters."
		if 'alphabet' not in errors:
			for c in postData['last_name']:
				if ord(c.lower()) < 97 or ord(c.lower())>122:
					errors['alphabet'] = "Names can only contain letters."
		if postData['pw'] != postData['pw_confirm']:
			errors['pw_mismatch'] = "Passwords don't match."
		if len(postData['pw'])<8:
			errors['pw_length'] = "Password too short."
		if not re.fullmatch(regex, postData['email']):
			errors['email'] = "Email not valid."
		if User.objects.filter(email=postData['email']):
			errors['user'] = 'User already exists.'

		d = datetime.datetime(year=int(postData['birthday_year']),
								month=int(postData['birthday_month']),
								day=int(postData['birthday_day']))

		if not UserManager.birthday_valid(d):
			errors['age'] = 'You are less than 13 years old'
		return errors
class User(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	email = models.EmailField()
	pw = models.CharField(max_length=100)
	birthday = models.DateTimeField()
	objects = UserManager()
class PostManager(models.Manager):
	def del_time(self, post_id):
		today = pytz.UTC.localize(datetime.datetime.now())
		created_time = Post.objects.get(id=post_id).created_at
		thirty_min = today - datetime.timedelta(minutes=30)
		if created_time < thirty_min:
			return False
		else:
			return True
class Post(models.Model):
	post_text = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	user = models.ForeignKey(User, related_name="posts", on_delete=models.CASCADE)
	objects = PostManager()
class Comment(models.Model):
	comment_text = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	post = models.ForeignKey(Post, related_name="post_comments", on_delete=models.CASCADE)
	user = models.ForeignKey(User, related_name="user_comments", on_delete=models.CASCADE)