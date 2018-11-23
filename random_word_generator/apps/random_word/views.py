from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

def index(request):
    if not request.session.values():
        request.session['counter'] = 0
    return render(request, 'random_word/index.html')

def generate(request):
    if request.method == 'POST':
        request.session['random'] = get_random_string(length=14)        
        request.session['counter'] += 1
        return render(request, 'random_word/index.html')
    else:
        request.session['random'] = request.session['random']
        request.session['counter']= request.session['counter']
        return redirect("/")

def reset(request):
    if request.method == 'POST':
        request.session['counter'] = 0
        request.session['random'] = ""
    return redirect("/")


    