import email
from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=30)
    lastname=models.CharField(max_length=30)
    username=models.CharField(max_length=30)
    email=models.EmailField(max_length=60,unique=True)
    password=models.CharField(max_length=60)
    salary=models.IntegerField()
    gender=models.CharField(max_length=1)
