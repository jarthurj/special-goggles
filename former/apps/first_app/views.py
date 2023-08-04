from django.shortcuts import render, HttpResponse

def index(request):
	return render(request, "first_app/index.html")

def info(request):
	context = {
		"name":request.POST['name'],
		"location":request.POST['loc'],
		"comments":request.POST['comment'],

	}
	return render(request, "first_app/info.html", context)
