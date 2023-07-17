from django.db import models

# Create your models here.


class AddStudent(models.Model):
    name = models.CharField(max_length = 25)
    age = models.IntegerField()
    address = models.CharField(max_length = 100)
    phone = models.BigIntegerField()
    gender = models.CharField(max_length = 10)
    education = models.CharField(max_length = 50)
    course = models.CharField(max_length = 30)
    course_id = models.CharField(max_length = 20, default = "")
    duration = models.CharField(max_length = 30)
    email = models.CharField(max_length = 50)
    username = models.CharField(max_length = 40)
    password = models.CharField(max_length = 20)
    course_id = models.CharField(max_length = 20, default = "")



class AddBatch(models.Model):
    name = models.CharField(max_length = 50)
    course = models.CharField(max_length = 25)
    duration = models.CharField(max_length = 20)


class AddTask(models.Model):
    name = models.CharField(max_length = 30)
    task = models.CharField(max_length = 50)
    description = models.CharField(max_length = 100)
    date = models.DateField()



class AddstudentBatch(models.Model):
    s_name = models.CharField(max_length = 25)
    b_name = models.CharField(max_length = 50)
    b_id = models.CharField(max_length = 20, default = "")
    
