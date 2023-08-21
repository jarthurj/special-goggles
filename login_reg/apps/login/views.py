from django.shortcuts import render, redirect
from .forms import UserForm, LoginForm
from .models import User
from django.contrib import messages
def index(request):
	context={
		'regForm':UserForm(),
		'loginForm':LoginForm(),
	}
	return render(request, 'login/login.html',context)

def process_reg(request):
	errors = User.objects.reg_validator(request.POST)
	print(errors)
	if errors:
		for key, value in errors:
			messages.error(request, value)
		return redirect('/login/')
	else:
		u = User.objects.create(first_name=request.POST['first_name'],
							last_name=request.POST['last_name'],
							email=request.POST['email'],
							pw=request.POST['pw'])
		request.session['user'] = u.id
		return redirect('/successreg/')

def success_reg(request):
	context = {
		'user':User.objects.get(id=request.session['user'])
	}
	return render(request, 'login/successreg.html', context)

def process_log(request):
	return redirect('/successreg/')

def success_log(request):
	context = {}
	return render(request, 'login/success.html', context)