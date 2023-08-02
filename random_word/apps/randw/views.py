from django.shortcuts import render, HttpResponse
from django.utils.crypto import get_random_string

def index(request):
	request.session['counter'] = 1
	context = {
		"rander": get_random_string(length=14),
		"count": request.session['counter'],
	}
	return render(request, "randw/index.html", context)

def randw(request):
	request.session['counter'] += 1
	context = {
		"rander": get_random_string(length=14),
		"count": request.session['counter'],
	}
	return render(request, "randw/index.html", context)
