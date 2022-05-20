from django.db import models

# Create your models here.
class team(models.Model):
    fullname=models.CharField(max_length=30)
    agelimit=models.IntegerField()
    sons=models.IntegerField(default=5)
    emailadd=models.EmailField(max_length=100)
    password=models.CharField(max_length=10)
    occupation=models.CharField(max_length=20,default='not available')


