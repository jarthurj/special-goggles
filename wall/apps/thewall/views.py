from django.shortcuts import render, redirect
from .forms import UserForm, LoginForm, PostForm, CommentForm
from .models import User, Post, Comment
from django.contrib import messages
import bcrypt
import datetime
def index(request):
	request.session.flush()
	context={
		'regForm':UserForm(),
		'loginForm':LoginForm(),
	}
	return render(request, 'thewall/login.html',context)

def process_reg(request):
	errors = User.objects.reg_validator(request.POST)
	print(errors)
	if errors:
		for key, value in errors.items():
			messages.error(request, value)
		return redirect('/')
	else:
		for key, value in request.POST.items():
			print(key, value)
		d = datetime.datetime(year=int(request.POST['birthday_year']),
								month=int(request.POST['birthday_month']),
								day=int(request.POST['birthday_day']))
		u = User.objects.create(first_name=request.POST['first_name'],
							last_name=request.POST['last_name'],
							email=request.POST['email'],
							pw=bcrypt.hashpw(request.POST['pw'].encode(),bcrypt.gensalt()).decode(),
							birthday=d)
		messages.success(request, "Registration Successful")
		return redirect('/')

def process_log(request):
	user = User.objects.filter(email=request.POST['email'])
	if len(user)==1:
		print(user[0].pw.encode('utf-8'))
		print(bcrypt.hashpw(request.POST['pw'].encode('utf-8'),bcrypt.gensalt()))
		pw_good = bcrypt.checkpw(request.POST['pw'].encode(), user[0].pw.encode())
		if pw_good:
			request.session['user'] = user[0].id
			return redirect('/wall/')
		else:
			return redirect('/')
	else:
		return redirect('/')

def wall(request):
	context={
		'post_form':PostForm(),
		'comment_form':CommentForm(),
		'posts':Post.objects.all(),
	}
	return render(request, 'thewall/wall.html', context)

def add_post(request):
	post_text = request.POST['post_text']
	Post.objects.create(post_text=post_text,user=User.objects.get(id=request.session['user']))
	return redirect('/wall/')

def add_comment(request):
	comment_text = request.POST['comment_text']
	Comment.objects.create(comment_text=comment_text,
							post=Post.objects.get(id=request.POST['post_id']),
							user=User.objects.get(id=request.session['user']))
	return redirect('/wall/')

def del_comment(request):
	print(request.GET['user_id'], type(request.GET['user_id']))
	print(request.session['user'], type(request.session['user']))
	if (request.session['user'] == int(request.GET['user_id']) and 
		Post.objects.del_time(int(request.GET['post_id']))):
			p = Post.objects.get(id=request.GET['post_id'])
			p.delete()
			return redirect('/wall/')
	else:
		messages.error(request,"POST TO OLD TO DELETE")
		return redirect('/wall/')
