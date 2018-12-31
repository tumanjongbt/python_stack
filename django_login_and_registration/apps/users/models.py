from django.db import models
import re
import bcrypt

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'^[a-zA-Z]+$')

# Create your models here.
# model field reference
class UserManager(models.Manager):
    # function to validate creation of a user. validate accepts form data from the user form
    def validate(self, form_data):
        errors = []
        if len(form_data['first_name']) < 2:
            errors.append("First name must be at least 2 characters long")
        if len(form_data['first_name']) < 2:
            errors.append("First name must be at least 2 characters long")
        if not NAME_REGEX.match(form_data['first_name']) or not NAME_REGEX.match(form_data['last_name']):
            errors.append("Name must contain letters only ")
        if not EMAIL_REGEX.match(form_data['email']):
            errors.append("Email must be valid")
        if len(form_data['password']) < 8:
            errors.append("Password must be at least 8 characters long")
        if form_data['password'] != form_data['confirm_password']:
            errors.append("Passwords mismatch - try again")
#check if user already exist

        if self.filter(email=form_data['email']):
            errors.append("Email already in use") 
        return errors

    def create_user(self, form_data):
        pw_hash=bcrypt.hashpw(form_data['password'].encode(), bcrypt.gensalt())
        return self.create(
            first_name=form_data['first_name'],
            last_name=form_data['last_name'],
            email=form_data['email'],
            pw_hash = pw_hash,
        )

    def check_login(self, form_data):
        # self.get is same as User.objects.get:  self.get will either return a valid user or an error
        # so use try except since there will be a high occurence of errors
        # Verify email exist
        # Verify encrypted password
            # If TRUE login is successful because password matches, return user_id and store in session
            # sessions is inaccessible from models
        errors = []
        try:
            user = self.get(email=form_data['email'])
        except:
            errors.append("Email or password invalid") 
            return (False, errors) # returns a tuple containing 2 values: Check fails, and error displayed 

        if bcrypt.checkpw(form_data['password'].encode(), user.pw_hash.encode()): #returns a boolean.  
            return (True, user)
        else:
            errors.append("Email or password invalid")
            return (False, errors)
        
class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    pw_hash = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True) #adds time only when new item is added
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager() # overrights user.objects with inherited user.objects from UserManager.  

    def __str__(self):
        return self.email
        