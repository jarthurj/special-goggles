from django.shortcuts import render, HttpResponse, redirect
from .forms import NameForm
from .models import Person
def index(request):
	context = {
		'users': Person.objects.all(),
	}
	return render(request, "user_crud/users.html", context)

def user(request, uid):
	context = {'user':Person.objects.get(id=uid)}
	return render(request, "user_crud/single_user.html", context)


def users_new(request):
	context = {
		'form': NameForm(),
	}
	return render(request, "user_crud/add_user.html", context)

def users_edit(request, uid):
	p = Person.objects.get(id=uid)
	context = {
	'user':p,
	'form': NameForm(initial={'first_name':p.first_name,
								'last_name':p.last_name,
								'email':p.email}),
	}
	return render(request, "user_crud/edit_user.html", context)

def users_create(request):
	p = Person.objects.create(first_name=request.POST['first_name'],
								last_name=request.POST['last_name'],
								email=request.POST['email'])
	return redirect("/users/")

def destroy(request, uid):
	p = Person.objects.get(id=uid)
	p.delete()
	return redirect("/users/")

def update(request, uid):
	p = Person.objects.get(id=uid)
	p.first_name=request.POST['first_name']
	p.last_name=request.POST['last_name']
	p.email=request.POST['email']
	p.save()
	return redirect("/users/")
