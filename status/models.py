from email.policy import default
from django.db import models

# Create your models here.
class Status(models.Model):
    name = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Todo(models.Model):
    name = models.CharField(max_length=20)
    status = models.ForeignKey(Status,on_delete= models.CASCADE,related_name='todos')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_completed = models.BooleanField(default=False)


    