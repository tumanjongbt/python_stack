from django.shortcuts import render, redirect
from time import localtime, strftime

# Create your views here.

def home(req):
    return render(req, 'session_words/index.html')

def create(req):
     
    time_created = strftime('%#H:%M:%S%p, %B, %#d %Y', localtime())

    temp_list = req.session['words']

    if 'big_font' in req.POST:
        showbig = 1
    else:
        showbig = 0
    temp_list.append({"time": time_created, "new_word": req.POST['word'], "color": req.POST['color'], "font_size": showbig })

    req.session['words'] = temp_list

    return redirect('/home')

def clear(req):
    req.session.clear()
    return redirect('/home')