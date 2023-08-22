from django.shortcuts import render, redirect
from .forms import UserForm, LoginForm
from .models import User
from django.contrib import messages
import bcrypt
import datetime
def index(request):
	request.session.flush()
	context={
		'regForm':UserForm(),
		'loginForm':LoginForm(),
	}
	return render(request, 'login/login.html',context)

def process_reg(request):
	errors = User.objects.reg_validator(request.POST)
	print(errors)
	if errors:
		for key, value in errors.items():
			messages.error(request, value)
		return redirect('/login/')
	else:
		for key, value in request.POST.items():
			print(key, value)
		d = datetime.datetime(year=int(request.POST['birthday_year']),
								month=int(request.POST['birthday_month']),
								day=int(request.POST['birthday_day']))
		u = User.objects.create(first_name=request.POST['first_name'],
							last_name=request.POST['last_name'],
							email=request.POST['email'],
							pw=bcrypt.hashpw(request.POST['pw'].encode(),bcrypt.gensalt()),
							birthday=d)
		request.session['user'] = u.id
		return redirect('/success/')

def success(request):
	return render(request, 'login/successreg.html')

def process_log(request):
	
	user = User.objects.filter(email=request.POST['email'])
	if len(user)==1:
		print(user[0].pw.encode())
		print(bcrypt.hashpw(str(request.POST['pw']).encode(),bcrypt.gensalt()))
		pw_good = bcrypt.checkpw(str(request.POST['pw']).encode(), user[0].pw.encode())
		if pw_good:
			return redirect('/success/')
		else:
			return redirect('/login/')
	else:
		return redirect('/login/')
