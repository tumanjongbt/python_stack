
from django.shortcuts import render, redirect
import datetime
import random

# Create your views here.

def index(request):
    try:
        request.session['total_gold']
    except KeyError:
        request.session['total_gold'] = 0
    try:
        request.session['activities']
    except KeyError:
        request.session['activities'] = []
    return render(request, 'ninjagame/index.html')

def process(request):
    if request.POST['action'] == "farm":
        print("===========FARM===============")
        earnings = random.randrange(10, 20)
        request.session['total_gold'] += earnings
        request.session['activities'].append(
            'Earned ' + str(earnings) + ' gold from the farm! (' +
            '{:%Y/%m/%d %I:%M %p})'.format(datetime.datetime.now())
        )
        if len(request.session['activities']) >= 8:
            request.session['activities'].pop(0)
        return redirect('/')

    elif request.POST['action'] == "cave":
        print("===========CAVE===============")
        earnings = random.randrange(5, 10)
        request.session['total_gold'] += earnings
        request.session['activities'].append(
            'Earned ' + str(earnings) + ' gold from the cave! (' +
            '{:%Y/%m/%d %I:%M %p})'.format(datetime.datetime.now())
        )
        if len(request.session['activities']) >= 8:
            request.session['activities'].pop(0)
        return redirect('/')

    elif request.POST['action'] == "house":
        print("===========HOUSE===============")
        earnings = random.randrange(2, 5)
        request.session['total_gold'] += earnings
        request.session['activities'].append(
            'Earned ' + str(earnings) + ' gold from the house! (' +
            '{:%Y/%m/%d %I:%M %p})'.format(datetime.datetime.now())
        )
        if len(request.session['activities']) >= 8:
            request.session['activities'].pop(0)
        print ("======len=========",len(request.session['activities']))
        return redirect('/')

    elif request.POST['action'] == "casino":
        print("===========CASINO===============")
        earnings = random.randrange(-50, 50)
        request.session['total_gold'] += earnings
        if earnings < 0:
            request.session['activities'].append(
                'Entered a casino and Won ' + str(earnings) + ' gold! Ouch! (' +
                '{:%Y/%m/%d %I:%M %p})'.format(datetime.datetime.now())
            )
        if len(request.session['activities']) >= 8:
            request.session['activities'].pop(0)
            return redirect('/')
        else:
            request.session['activities'].append(
                'Entered a casino and Lost ' + str(earnings) + ' gold. Holy Cow! (' +
                '{:%Y/%m/%d %I:%M %p})'.format(datetime.datetime.now())
            )
            if len(request.session['activities']) >= 8:
                request.session['activities'].pop(0)
                return redirect('/')
            else:
                return redirect('/')
    
def reset(request):
    request.session['total_gold'] = 0
    request.session['activities'].clear()

    return render(request, 'ninjagame/index.html')