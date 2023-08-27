from django.shortcuts import render, HttpResponse

def index(request):
	request.session.flush()
	return render(request, "dash/index.html")

def login(request):
	request.session.flush()
	context={
	}
	return render(request, "dash/login.html",context)

def register(request):
	return render(request, "dash/register.html")

def admin(request):
	return render(request, "dash/admin.html")

def dashboard(request):
	return render(request, "dash/dashboard.html")

def show(request):
	return render(request, "dash/show.html")

def edit(request):
	return render(request, "dash/edit.html")

def admin_edit(request):
	return render(request, "dash/admin_edit")


#method for registering user.
def register_user(request):
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