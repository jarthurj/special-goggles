from django import forms

YEARS = [y for y in range(1900, 2023)]

class UserForm(forms.Form):
	first_name = forms.CharField(max_length=50)
	last_name = forms.CharField(max_length=50)
	email = forms.CharField(max_length=50)
	pw = forms.CharField(max_length=50, widget=forms.PasswordInput)
	pw_confirm = forms.CharField(max_length=50, widget=forms.PasswordInput)
	birthday = forms.DateTimeField(widget=forms.SelectDateWidget(years=YEARS))
class LoginForm(forms.Form):
	email = forms.CharField(max_length=50)
	pw = forms.CharField(max_length=50, widget=forms.PasswordInput)
