from django.shortcuts import render, HttpResponse
from time import time, strftime, gmtime
def index(request):
	context = {
		"time_and_date":strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime()),
	}
	return render(request, "first_app/index.html", context)