from django.db import models
from django.core.validators import MaxLengthValidator
from django.contrib.auth.models import User
# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=80, validators=[MaxLengthValidator])
    memo = models.TextField(blank=True)
    is_important = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    datecompleted = models.DateTimeField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='todos')
    is_completed = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title
