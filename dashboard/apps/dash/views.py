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
	return render(request, "dash/login.html")

def register(request):
	return render(request, "dash/register.html")

def admin(request):
	return render(request, "dash/admin.html")

def dashboard(request):
	context = {
		'users': User.objects.all(),
		'user_first_name': User.objects.get(id=request.session['user']).first_name
	}
	if User.objects.get(id=request.session['user']).user_level==0:
		return render(request, "dash/dashboard.html", context)
	else:
		return render(request, "dash/admin-dashboard.html", context)
def show(request, uid):
	context={
		"posts":Post.objects.filter(post_user=User.objects.get(id=uid)),
		"user":User.objects.get(id=uid),
	}
	return render(request, "dash/show.html", context)

def edit(request):
	context = {
		'user':User.objects.get(id=request.session['user'])
	}
	return render(request, "dash/edit.html", context)

def admin_edit(request, uid):
	context = {
		'user':User.objects.get(id=uid),
	}

	return render(request, "dash/admin_edit.html",context)




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
		pw_good = bcrypt.checkpw(request.POST['pw'].encode(), user[0].pw.encode())
		if pw_good:
			request.session['user'] = user[0].id
			return redirect('/dashboard/')
		else:
			return redirect('/index/')
	else:
		return redirect('/index/')

def add_post(request):
	for key,value in request.POST.items():
		print(key,value)
	post_text = request.POST['post_text']
	Post.objects.create(post_text=post_text,
						user=User.objects.get(id=request.session['user']),
						post_user=User.objects.get(id=int(request.POST['post_user'])))
	return redirect('show', uid=int(request.POST['post_user']))

def add_comment(request):
	comment_text = request.POST['comment_text']
	c = Comment.objects.create(comment_text=comment_text,
							post=Post.objects.get(id=request.POST['post_id']),
							user=User.objects.get(id=request.session['user']))
	return redirect('show', uid=c.post.post_user.id)

def edit_pw(request):
	errors = User.objects.pw_validator(request.POST)
	if errors:
		for key, value in errors.items():
			messages.error(request, value)
		return redirect('/edit/')
	else:
		pw = bcrypt.hashpw(request.POST['pw'].encode(),bcrypt.gensalt()).decode()
		u = User.objects.get(id=request.session['user'])
		u.pw = pw
		u.save()
		messages.success(request, "Registration Successful")
		return redirect('/edit/')

def edit_user(request):
	errors = User.objects.user_validator(request.POST)
	if errors:
		for key, value in errors.items():
			messages.error(request, value)
		return redirect('/edit/')
	else:
		u = User.objects.get(id=request.session['user'])
		u.first_name = request.POST['first_name']
		u.last_name = request.POST['last_name']
		u.email = request.POST['email']
		u.save()
		messages.success(request, "Registration Successful")
		return redirect('/edit/')

def admin_edit_user(request):
	print('asssssssssssssssssss')
	for key, value in request.POST.items():
			print(key, value)
	errors = User.objects.user_validator(request.POST)
	if errors:
		for key, value in errors.items():
			messages.error(request, value)
		return redirect('admin_edit', uid=request.POST['id'])
	else:
		u = User.objects.get(id=request.POST['id'])
		u.first_name = request.POST['first_name']
		u.last_name = request.POST['last_name']
		u.email = request.POST['email']
		u.save()
		messages.success(request, "User Info Update Successful")
		return redirect('admin_edit',uid=request.POST['id'])


def admin_edit_password(request):
	errors = User.objects.pw_validator(request.POST)
	if errors:
		for key, value in errors.items():
			messages.error(request, value)
		return redirect('admin_edit', uid=request.POST['id'])
	else:
		pw = bcrypt.hashpw(request.POST['pw'].encode(),bcrypt.gensalt()).decode()
		u = User.objects.get(id=request.POST['id'])
		u.pw = pw
		u.save()
		messages.success(request, "Password Change Successful")
		return redirect('admin_edit', uid=request.POST['id'])
def delete_user(request,uid):
	u=User.objects.get(id=uid)
	u.delete()
	return redirect('/dashboard/')
