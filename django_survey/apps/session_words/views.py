from django.shortcuts import render, redirect
from time import localtime, strftime

# Create your views here.

def new(req):
    return render(req, 'session_words/index.html')

def create(req):
     
    time_created = strftime('%#H:%M:%S%p, %B, %#d %Y', localtime())

    temp_list = []
    req.session['words'] = []

    if 'big_font' in req.POST:
        showbig = 10
        temp_list.append({"time": time_created, "new_word": req.POST['word'], "color": req.POST['color'], "font_size": showbig })

    else:
        showbig = 5
        temp_list.append({"time": time_created, "new_word": req.POST['word'], "color": req.POST['color'], "font_size": showbig })


    req.session['words'] = temp_list

    print(req.session['words'])

    # return redirect('/session_words/index')
    return redirect('/session_words/new')
def clear(req):
    req.session.clear()
    return redirect('/session_words/new')