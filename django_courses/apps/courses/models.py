from django.db import models

# Create your models here.

class CourseManager(models.Manager):
	def validate(self, form_data):
		errors = []
		if len(form_data['name']) < 6:
			errors.append("Course name must be at least 6 characters long")
		if len(form_data['description']) < 16:
			errors.append("Course description must be at least 16 characters long")
		return errors

	def create_course(self, form_data):
		return self.create(
			name=form_data['name'],
			description=form_data['description']
		)	
	
	def delete_course(self, course_id):
		course = Course.objects.get(id=course_id)
		course.delete()

# class DescriptionManager(models.Manager):
# 	def create_description(self, form_data):
# 		return self.create(
# 			description=form_data['description']
# 		)	

# class Description(models.Model):
# 		description = models.TextField()	    
# 		created_at = models.DateTimeField(auto_now_add=True)
# 		updated_at = models.DateTimeField(auto_now=True)
# 		objects = DescriptionManager()

class Course(models.Model):
		name = models.CharField(max_length=255)
		# description = models.OneToOneField(Description, related_name="descriptions")
		description = models.TextField()	    
		created_at = models.DateTimeField(auto_now_add=True)
		updated_at = models.DateTimeField(auto_now=True)
		objects = CourseManager()

		def __str__(self):
				return self.name