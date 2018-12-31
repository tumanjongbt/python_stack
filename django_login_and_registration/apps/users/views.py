from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User

# Create your views here.
def new(req):
    return render(req, 'users/new.html')

def create(req):
    # outsource all the business logic to the models.py file.  It will have the validation, queries
    # views will simply shuffle the information.
    # methods that are written in the classes residing in the models.py file must be imported inside the views file.
    # Information from the classes are returned to the functions here.

    errors = User.objects.validate(req.POST) #returned errors from the validate method in models.py
    if errors:
        for error in errors:
            messages.error(req, error)
        return redirect('users:new')
    #Register and login user
    user = User.objects.create_user(req.POST) #returned information from the create_user method in models.py
    req.session['user_id'] = user.id
    
    req.session['message'] = []
    if req.POST['action'] == "registered":
        req.session['message'].append(
            'Successfully registered')
        
    context = {
        'user_info':User.objects.get(id=req.session['user_id']),
        'message': req.session['message']
    }
    
    return render(req, 'users/success.html', context) 

def login(req):
    #if fail:
    valid, result = User.objects.check_login(req.POST) #tuple unpacking. valid - TRUE/FALSE: result - user/errors
    if not valid:
        for error in result:
            messages.error(req, error)
        return redirect('users:new')

    req.session['user_id'] = result.id

    req.session['message'] = []
    if req.POST['action'] == "logged in":
        req.session['message'].append(
            'Successfully logged in')
        
    context = {
        'user_info':User.objects.get(id=req.session['user_id']),
        'message': req.session['message']
    }
    
    return render(req, 'users/success.html', context) 

def logout(req):
    if 'user_id' not in req.session:
        return redirect('users:new')
    else:
        req.session.clear()
        return redirect('users:new')
