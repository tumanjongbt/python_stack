from django.db import models


# import re

# EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# Create your models here.
# model field reference
# class UserManager(models.Manager):
#     # function to validate creation of a user. validate accepts form data from the user form
#     def validate(self):
#         errors = []
#         if len('first_name') < 2:
#             errors.append("First name must be at least 2 characters long")
#         if len('last_name') < 2:
#             errors.append("Last name must be at least 2 characters long")
#         if not EMAIL_REGEX.match('email'):
#             errors.append("Email must be valid")
# #check if user already exist
#         if self.filter(email='email'):
#             errors.append("Email already in use") 
#         return errors

class User(models.Model):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	email_address= models.CharField(max_length=255)
	age = models.IntegerField()
	created_at = models.DateTimeField(auto_now_add=True) #adds time only when new item is added
	updated_at = models.DateTimeField(auto_now=True)
	# objects = UserManager() # connects User to UserManager.  

	def __str__(self):
		return self.email_address
		