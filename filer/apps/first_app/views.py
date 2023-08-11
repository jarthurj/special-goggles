from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from .forms import UploadFileForm
from .file_handler import handle_uploaded_file
def index(request):
	context = {
		'form':UploadFileForm()
	}
	return render(request, "first_app/index.html", context)


def file(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES["file"])
            return HttpResponseRedirect("/success/")
    else:
        form = UploadFileForm()
    return render(request, "first_app/index.html", {"form": form})

def success(request):
	return HttpResponse("file upload successful")