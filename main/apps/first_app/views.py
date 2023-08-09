from django.shortcuts import render, HttpResponse, redirect


def index(request):
	response = "Fplaceholder to later display all the list of blogs"
	return HttpResponse(response)

def new(request):
	response = "place holder to display a new form to creat a new blog"
	return HttpResponse(response)

def create(request):
	return redirect("index")

def blog_by_number(request, blog):
	return HttpResponse(f'place holder to display blog {blog}')

def edit_blog(request, blog):
	return HttpResponse(f"place holder to edit blog {blog}")

def delete(request, blog):
	return redirect("index")
