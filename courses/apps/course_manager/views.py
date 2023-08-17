from django.shortcuts import render, HttpResponse, redirect
from .models import Course, Description
from .forms import CourseForm
def index(request):
	context = {
		'courses':Course.objects.all(),
		'form':CourseForm(),
	}
	return render(request, "course_manager/index.html", context)

def add_course(request):
	d = Description.objects.create(description=request.POST['course_description'])
	Course.objects.create(name=request.POST['course_name'], desc=d)
	return redirect("/")

def destroy(request,uid):
	c = Course.objects.get(id=uid)
	c.delete()
	return redirect("/")