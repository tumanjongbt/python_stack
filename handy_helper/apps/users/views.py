from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User

def index(req):
    return render(req, 'users/index.html')

def create(req):

    errors = User.objects.validate_user(req.POST) 
    if errors:
        for error in errors:
            messages.error(req, error)
        return redirect('users:index')
    user = User.objects.create_user(req.POST) 
    req.session['user_id'] = user.id
    return redirect('jobs:dashboard') 

def login(req):
    valid, result = User.objects.login_user(req.POST) 
    if not valid:
        for error in result:
            messages.error(req, error)
        return redirect('users:index')

    req.session['user_id'] = result.id
    return redirect('jobs:dashboard')

def logout(req):
    req.session.clear()
    return redirect('users:index')
