from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(req):
    # if not 'counter'in req.session.keys():
    #     req.session['counter'] = 0
    return render(req, "surveys/index.html")

def survey(req):
    if req.method == 'POST':      
        req.session['counter'] += 1
        req.session['name'] = req.POST['name']
        req.session['location'] = req.POST['location']
        req.session['language'] = req.POST['language']
        req.session['message'] = req.POST['message']
        return redirect("/result")
    else:
        return redirect("/")

def result(req):
    context = {
        'counter': req.session['counter'],
        'name': req.session['name'],
        'location': req.session['location'],
        'language': req.session['language'],
        'message': req.session['message'],
    }
    return render(req, "surveys/result.html", context)

def back(req):
    if req.method == 'POST': 
        return redirect("/")
  







    