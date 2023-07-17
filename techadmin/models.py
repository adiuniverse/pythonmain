from django.db import models

# Create your models here.
class Teachers(models.Model):
    name = models.CharField(max_length = 20)
    phone = models.BigIntegerField()
    address = models.CharField(max_length = 100)
    gender = models.CharField(max_length = 10)
    email = models.CharField(max_length = 25)
    username = models.CharField(max_length = 25)
    password = models.CharField(max_length = 25)
    experience = models.CharField(max_length = 25)



class Course(models.Model):
    name = models.CharField(max_length = 50)
    duration = models.CharField(max_length = 20)
    price = models.FloatField()
    image = models.ImageField(upload_to = 'course/')


class Batch(models.Model):
    name = models.CharField(max_length = 20)
    day = models.CharField(max_length = 20)
    start = models.CharField(max_length = 20)
    end = models.CharField(max_length = 20)