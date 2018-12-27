from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Course

# Create your views here.

def index(req):
	# if 'course_id' not in req.session:
	# 	return redirect('courses:index')

	# if 'description_id' not in req.session:
	# 	return redirect('courses:index')

	context = {
		'course_list': Course.objects.all()
	}
	return render(req, 'courses/index.html', context)

def create(req):
	errors = Course.objects.validate(req.POST)
	if errors:
		for error in errors:
			messages.error(req, error)
		return redirect('courses:index')
	# Add a course
	# description = Description.objects.create_description(req.POST)
	course = Course.objects.create_course(req.POST)
	# Course.objects.get(id=course.id).descriptions.add(Description.objects.get(id=description.id))

	req.session['course_id'] = course.id
	# req.session['description_id'] = description.id

	return redirect('courses:index')

def destroy(req, course_id):
	if 'course_id' not in req.session:
		return redirect('courses:index')

	try:
		course = Course.objects.get(id=course_id)
	except:
		return redirect('courses:index')

	context = {
		'course': course
	}
	return render(req, 'courses/destroy.html', context)

def delete(req, course_id):
	Course.objects.delete_course(course_id)
	return redirect('courses:index')
