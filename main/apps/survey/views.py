from django.shortcuts import render, HttpResponse

def index(request):
	return HttpResponse("survey")

def surveys(request):
	return HttpResponse("placeholder to display all the surveys created")

def new(request):
	return HttpResponse("placeholder for users to add a new survey")

    # /surveys - display "placeholder to display all the surveys created"
    # /surveys/new - display "placeholder for users to add a new survey"
