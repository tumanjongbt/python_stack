from django.db import models
import re
import bcrypt

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'^[a-zA-Z]+$')

class UserManager(models.Manager):
    def validate_user(self, form_data):
        errors = []
        if len(form_data['first_name']) < 2:
            errors.append("First name must be at least 2 characters long")
        if len(form_data['last_name']) < 2:
            errors.append("Last name must be at least 2 characters long")
        if not NAME_REGEX.match(form_data['first_name']) or not NAME_REGEX.match(form_data['last_name']):
            errors.append("Invalid Name - must contain letters only ")
        if not EMAIL_REGEX.match(form_data['email']):
            errors.append("Email must be valid")
        if len(form_data['password']) < 8:
            errors.append("Password must be at least 8 characters long")
        if form_data['password'] != form_data['confirm_password']:
            errors.append("Passwords mismatch - try again")
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

    def login_user(self, form_data):
        errors = []
        try:
            user = self.get(email=form_data['email'])
        except:
            errors.append("Email or password invalid") 
            return (False, errors) 
        if bcrypt.checkpw(form_data['password'].encode(), user.pw_hash.encode()):  
            return (True, user)
        else:
            errors.append("Email or password invalid")
            return (False, errors)
        
class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    pw_hash = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager() 

    def __str__(self):
        return self.email
        