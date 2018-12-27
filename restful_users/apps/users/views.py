from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User

# Create your views here.

def index(req):
	if 'user_id' not in req.session:
		return redirect('users:new')

	context = {
  'user_list': User.objects.all()
	}
	return render(req, 'users/index.html', context)

def new(req):
	return render(req, 'users/new.html')

def create(req):
  errors = User.objects.validate(req.POST)
  if errors:
    for error in errors:
      messages.error(req, error)
    return redirect('users:new')
  # create and login user
  user = User.objects.create_user(req.POST)
  req.session['user_id'] = user.id
  return redirect('users:index')

def login(req):
  valid, result = User.objects.check_login(req.POST)
  if not valid:
    for error in result:
      messages.error(req, error)
    return redirect('users:new')

  req.session['user_id'] = result.id
  return redirect('users:index')

def logout(req):
  req.session.clear()
  return redirect('users:new')

def show(req, user_id):
	if 'user_id' not in req.session:
		return redirect('users:index')

	try:
		user = User.objects.get(id=user_id)
	except:
		return redirect('users:index')

	context = {
		'user': user
	}
	return render(req, 'users/show.html', context)

def edit(req, user_id):
	if 'user_id' not in req.session:
		return redirect('users:index')

	try:
		context = {
			'user': User.objects.get(id=user_id)
		}
	except:
		return redirect('users:index')

	return render(req, 'users/edit.html', context)

def update(req, user_id):
	if 'user_id' not in req.session:
		return redirect('users:index')
		
	if req.method != 'POST':
		return redirect('users:edit', user_id)

	errors = User.objects.validate(req.POST)
	if errors:
		for error in errors:
			messages.error(req, error)
		return redirect('users:edit', user_id)
	
	User.objects.update_user(req.POST, user_id)
	return redirect('users:index')

def delete(req, user_id):
	User.objects.delete_user(user_id)
	return redirect('users:index')



	