from django import forms

class UserForm(forms.Form):
	first_name = forms.CharField(max_length=50)
	last_name = forms.CharField(max_length=50)
	email = forms.CharField(max_length=50)
	pw = forms.CharField(max_length=50, widget=forms.PasswordInput)
	pw_confirm = forms.CharField(max_length=50, widget=forms.PasswordInput)

class LoginForm(forms.Form):
	email = forms.CharField(max_length=50)
	pw = forms.CharField(max_length=50, widget=forms.PasswordInput)
