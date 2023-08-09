from django.shortcuts import render, HttpResponse, redirect

def index(request):
	return HttpResponse("users")

def register(request):
	return HttpResponse("placeholder for users to create a new user record")

def login(request):
	return HttpResponse('placeholder for users to login')

def new(request):
	return redirect("user/register/")

def users(request):
	return HttpResponse("place holder to later display all the list of users")

