from django.db import models
from ..users.models import User

# Create your models here.
class JobManager(models.Manager):
	def validate_job(self, form_data, user_id):
		errors = []
		if len(form_data['title']) < 3:
			errors.append('Job title must be at least 3 characters')
		if len(form_data['description']) < 10:
			errors.append('Description must be at least 10 characters')
		if len(form_data['location']) == 0:
			errors.append('A valid location is needed')

		if len(errors) > 0:
			return {'errors': errors}
		else:
			Job.objects.create(
				title = form_data['title'],
				description = form_data['description'],
				location = form_data['location'],
				creator = User.objects.get(id=user_id)
			)
			return {}
			
	def validate_edit(self, form_data, job_id):
		errors = []
		if len(form_data['title']) < 3:
			errors.append('Job title must be at least 3 characters')
		if len(form_data['description']) < 10:
			errors.append('Description must be at least 10 characters')
		if len(form_data['location']) == 0:
			errors.append('A valid location is needed')

		if len(errors) > 0:
			return {'errors': errors, 'id':job_id}
		else:
			job = Job.objects.get(id=job_id)
			job.title = form_data['title']
			job.description = form_data['description']
			job.location = form_data['location']
			job.save()
			return {}

	def delete_job(self, job_id):
		ticket = Job.objects.get(id=job_id)
		ticket.delete()

class Job(models.Model):
	title = models.CharField(max_length=255)
	description = models.CharField(max_length=255)
	location = models.CharField(max_length=255)
	creator = models.ForeignKey(User, related_name = "created_jobs")
	all_users = models.ManyToManyField(User, related_name = "all_jobs")
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = JobManager()
