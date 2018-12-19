from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __repr__(self):
        return "<User object: {}>".format(self.first_name)
    
class Book(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField()
    uploader = models.ForeignKey(User, related_name="uploaded_books") #one-to-many
    liked_user = models.ManyToManyField(User, related_name="liked_books") #many-to-many
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return "<Book object: {}>".format(self.name)
