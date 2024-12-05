from django.db import models

# Create your models here.

class Users(models.Model):
    login = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

class Products(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField(max_length=100)