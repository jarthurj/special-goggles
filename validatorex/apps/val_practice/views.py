from django.shortcuts import render, redirect
from .forms import RegForm
def index(request):
	context = {
		'form':RegForm(),
	}
	return render(request,'val_practice/index.html',context)

def register(request):
	if request.method == "POST":
		bound_form = RegForm(request.POST)
		if bound_form.is_valid():
			return redirect('success')

def success(request):
	return render(request,'val_practice/success.html')