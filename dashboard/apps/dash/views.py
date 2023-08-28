from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import User, Post, Comment
import bcrypt
import datetime
def index(request):
	request.session.flush()
	return render(request, "dash/index.html")

def login(request):
	request.session.flush()
	context={
	}
	return render(request, "dash/login.html",context)

def register(request):
	return render(request, "dash/register.html")

def admin(request):
	return render(request, "dash/admin.html")

def dashboard(request):
	context = {
		'users': User.objects.all()
	}
	return render(request, "dash/dashboard.html", context)

def show(request, uid):
	context={
		"posts":Post.objects.filter(user=User.objects.get(id=uid)),
		"user":User.objects.get(id=uid),
	}
	return render(request, "dash/show.html", context)

def edit(request):
	return render(request, "dash/edit.html")

def admin_edit(request):
	return render(request, "dash/admin_edit")


#method for registering user.
def register_user(request):
	errors = User.objects.reg_validator(request.POST)
	print(errors)
	if errors:
		for key, value in errors.items():
			messages.error(request, value)
		return redirect('/register/')
	else:
		d = datetime.datetime(year=1990,
								month=1,
								day=1)
		u = User.objects.create(first_name=request.POST['first_name'],
							last_name=request.POST['last_name'],
							email=request.POST['email'],
							pw=bcrypt.hashpw(request.POST['pw'].encode(),bcrypt.gensalt()).decode(),
							birthday=d,
							user_level=User.objects.get_user_level())
		messages.success(request, "Registration Successful")
		return redirect('/index/')

def login_user(request):
	user = User.objects.filter(email=request.POST['email'])
	if len(user)==1:
		print(user[0].pw.encode('utf-8'))
		print(bcrypt.hashpw(request.POST['pw'].encode('utf-8'),bcrypt.gensalt()))
		pw_good = bcrypt.checkpw(request.POST['pw'].encode(), user[0].pw.encode())
		if pw_good:
			request.session['user'] = user[0].id
			return redirect('/dashboard/')
		else:
			return redirect('/index/')
	else:
		return redirect('/index/')

def add_post(request):
	for x,y in request.POST.items():
		print(x,y)
	post_text = request.POST['post_text']

	Post.objects.create(post_text=post_text,user=User.objects.get(id=request.session['user']))
	return redirect('/dashboard/')

def add_comment(request):
	comment_text = request.POST['comment_text']
	Comment.objects.create(comment_text=comment_text,
							post=Post.objects.get(id=request.POST['post_id']),
							user=User.objects.get(id=request.session['user']))
	return redirect('/dashboard/')
