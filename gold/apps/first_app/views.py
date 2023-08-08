from django.shortcuts import render, HttpResponse
from random import randrange
def index(request):
	request.session.flush()
	request.session['gold'] = 0
	request.session['activities'] = []
	return render(request, "first_app/index.html")

def process_gold(request):
	for key in request.POST:
		print(key)
	if 'farm' in request.POST:
		gold_found = randrange(10,20)
		request.session['gold'] += gold_found
		request.session['activities'].append(f"You found {gold_found}gold in the farm.")
		print(gold_found)
	elif 'cave' in request.POST:
		gold_found = randrange(5,10)
		request.session['gold'] += gold_found
		request.session['activities'].append(f"You found {gold_found}gold in the cave.")
		print(gold_found)
	elif 'house' in request.POST:
		gold_found = randrange(2,5)
		request.session['gold'] += gold_found
		request.session['activities'].append(f"You found {gold_found}gold in the house.")
		print(gold_found)
	elif 'casino' in request.POST:
		gold_found = randrange(-50,50)
		request.session['gold'] += gold_found
		if gold_found >=0:
			request.session['activities'].append(f"You won {gold_found}gold in the casino.")
		else:
			request.session['activities'].append(f"You lost {gold_found}gold in the casino.")
		print(gold_found)
	context = {
		"gold":request.session['gold'],
		"activities":request.session["activities"]
	}
	return render(request, "first_app/index.html", context)