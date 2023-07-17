from django.db import models
from django.core.validators import MaxLengthValidator
# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=80, validators=[MaxLengthValidator])
    memo = models.TextField(blank=True,max_length=500, validators=[MaxLengthValidator])
    is_important = models.BooleanField()
