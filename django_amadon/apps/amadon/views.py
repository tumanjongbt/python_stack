from django.shortcuts import render, redirect

def index(request):
	return render(request, 'amadon/index.html')

def buy(request):
	
	if 'total_spent' not in request.session:
		request.session['total_spent'] = 0
	if 'total_ordered' not in request.session:
		request.session['total_ordered'] = 0
		
	request.session['prize'] = 0    

	if request.method == "POST":
		request.session['product'] = request.POST.get('product_id')
		request.session['quantity'] = request.POST.get('quantity')
		item_prize= {
			"1001" : 19.99,
			"1002" : 29.99,
			"1003" : 4.99,
			"1004" : 49.99
		}
		for key, value in item_prize.items():
			if request.session['product'] == key:
				request.session['prize'] = value
		request.session['purchase_prize'] = round(float(request.session['prize']) * int(request.session['quantity']), 2)
		request.session['total_spent'] += round(float(request.session['purchase_prize']), 2)
		request.session['total_ordered'] += int(request.session['quantity'])
		return redirect('amadon:checkout')

	else:
		return redirect('amadon:index')

def checkout(request):
	return render(request, 'amadon/checkout.html')