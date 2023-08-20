from django.shortcuts import render,redirect,reverse
from .models import Item
from decimal import Decimal
def index(request):
	context = {
		"items":Item.objects.all(),
	}
	# request.session['grand_total'] = Decimal('0')
	if 'grand_total' not in request.session:
		request.session['grand_total'] = '0'
	if 'grand_quantity' not in request.session:
		request.session['grand_quantity'] = 0
	return render(request, "amazern/index.html", context)

def buy(request):
	quantity = int(request.POST['quantity'])
	purchase_total = Item.objects.get(id=int(request.POST['itemId'])).price*quantity
	request.session['grand_total'] = str(Decimal(request.session['grand_total'])+Decimal(purchase_total))
	request.session['grand_quantity'] += quantity
	request.session['this_purchase'] = str(purchase_total)
	request.session['this_quantity'] = quantity
	return redirect("/thanks/")

def thanks(request):
	context = {
		'sesh':request.session,
	}
	return render(request, "amazern/thanks.html", context)