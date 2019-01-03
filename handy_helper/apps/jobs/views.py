from django.shortcuts import render, redirect
from .models import Job
from ..users.models import User
from django.contrib import messages

def dashboard(req):
    if 'user_id' not in req.session:
        return redirect('users:index')
    current_user = User.objects.get(id = req.session['user_id'])
    context = {
        'user': current_user,
        'current_user_job_list': Job.objects.filter(all_users = current_user),
        'jobs_list' : Job.objects.exclude(all_users = current_user),
    }
    return render(req, "jobs/dashboard.html", context)

def addjob(req):
    return render(req, 'jobs/addjob.html')

def create(req):
    result = Job.objects.validate_job(req.POST, req.session['user_id'])
    if 'errors' in result:
        for error in result['errors']:
            messages.error(req, error)
        return redirect('jobs:addjob')
    return redirect('jobs:dashboard')

def myjobs(req, job_id):
    current_user = User.objects.get(id=req.session['user_id'])
    job = Job.objects.get(id=job_id)
    job.all_users.add(current_user)
    job.save()
    return redirect('jobs:dashboard')

def view(req, job_id):
    context={
        'job': Job.objects.get(id=job_id)
    }
    return render(req, 'jobs/view.html', context)

def edit(req, job_id):
    if 'user_id' not in req.session:
        return redirect('jobs:dashboard')
    try:
        context = {
            'job': Job.objects.get(id=job_id)
        }
    except:
        return redirect('jobs:dashboard')
    return render(req, 'jobs/edit.html', context)

def update(req, job_id):
    result = Job.objects.validate_edit(req.POST, job_id)
    if 'errors' in result:
        for error in result['errors']:
            messages.error(req, error)
            return redirect('jobs:edit', job_id)
    return redirect('jobs:dashboard')

def delete(req, job_id):
    Job.objects.delete_job(job_id)
    return redirect('jobs:dashboard')
