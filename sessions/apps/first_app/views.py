from django.shortcuts import render, HttpResponse
from time import time, strftime, gmtime
def index(request):
	return render(request, 'first_app/index.html')


def add(request):
	temp_dict = {}
	temp_dict['word'] = request.POST['word']
	temp_dict['color'] = request.POST['color']
	try:
		temp_dict['big_font'] = request.POST['big_font']
			
	except:
		temp_dict['big-font'] = 0
	temp_dict['time'] = strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
	temp_list = []
	temp_list.append(temp_dict)
	request.session['word_list'] = temp_list
	context = {
		'word_list': temp_list,
		'ass': "ass", 
	}
	return render(request, 'first_app/add.html', context)
