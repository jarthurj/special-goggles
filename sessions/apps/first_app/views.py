from django.shortcuts import render, HttpResponse
from time import time, strftime, gmtime
def index(request):
	request.session.flush()
	return render(request, 'first_app/index.html')


def add(request):
	temp_dict = {}
	temp_dict['word'] = request.POST['word']
	temp_dict['color'] = request.POST['color']
	try:
		temp_dict['big_font'] = request.POST['big_font']
		temp_dict['big_font'] = True

	except:
		temp_dict['big-font'] = False

	try:
		temp_list = request.session['word_list']
	except:
		temp_list = []
	temp_dict['time'] = strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())

	temp_list.append(temp_dict)
	context = {
		'word_list': temp_list,
		'ass': "ass", 
	}
	return render(request, 'first_app/add.html', context)
