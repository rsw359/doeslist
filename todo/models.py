from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model

class Todo(models.Model):
    title = models.CharField(max_length=100)
    customer_name = models.CharField(max_length=100)
    customer_email = models.EmailField(blank=True, null=True)
    createdby = models.ForeignKey('doeslist.CustomUser', on_delete=models.CASCADE)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.title} - {self.customer_name}"
    
class CustomUser(AbstractUser):
    email = models.EmailField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.username
