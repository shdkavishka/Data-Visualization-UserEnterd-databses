from django.db import models

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=1000)
    email= models.EmailField()
    bio = models.CharField(max_length=1000)
    age = models.PositiveIntegerField()
    
class Student(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    
