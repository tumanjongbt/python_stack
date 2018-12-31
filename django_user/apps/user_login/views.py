from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import User
from django.core import serializers
import json

def index(request):
    return render(request, 'user_login/index.html')
# Create your views here.

def all_json(request):
	users = User.objects.all()
	users_json = serializers.serialize("json", users)
	return HttpResponse(users_json, content_type='application/json')

def all_html(request):
	users = User.objects.all()
	return render(request, 'user_login/all.html', { "users": users })

def find(request):
    return render(request, 'user_login/all.html',
        { "users": User.objects.filter(first_name__startswith=request.POST['first_name_starts_with']) }
    )

def create(request):
    User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email_address=request.POST['email_address'], age=request.POST['age'])
    return render(request, 'user_login/all.html',{ "users": User.objects.order_by("-id") })