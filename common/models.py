from django.db import models

# Create your models here.


class Techadmin(models.Model):
    name = models.CharField(max_length = 20)
    username = models.CharField(max_length = 25)
    password = models.CharField(max_length = 20)





class Trainer(models.Model):
    name = models.CharField(max_length = 20)
    email = models.CharField(max_length = 25)
    address = models.CharField(max_length = 100)
    phone = models.BigIntegerField()
    gender = models.CharField(max_length = 10)
    username = models.CharField(max_length = 25)
    password = models.CharField(max_length = 20)





class Student(models.Model):
    name = models.CharField(max_length = 20)
    email = models.CharField(max_length = 25)
    address = models.CharField(max_length = 100)
    phone = models.BigIntegerField()
    gender = models.CharField(max_length = 10)
    username = models.CharField(max_length = 25)
    password = models.CharField(max_length = 20)


class Contact(models.Model):
    name = models.CharField(max_length = 30)
    email = models.CharField(max_length = 25)
    subject = models.CharField(max_length = 100)
    message = models.CharField(max_length = 200)
    