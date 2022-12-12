from django.db import models

# Create your models here.

class Users(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.BigIntegerField()
    password = models.CharField(max_length=100)

    class Meta:
        db_table = 'users'

    
class Bookings(models.Model):
    user  = models.ForeignKey(Users, on_delete=models.CASCADE)
    plan = models.CharField(max_length=100)
    phone = models.BigIntegerField()
    car_name = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    washing_date = models.DateField()
    hour = models.IntegerField()
    minute = models.IntegerField()
    ampm = models.CharField(max_length=100)
    message = models.CharField(max_length=500) 
    status = models.CharField(max_length=500) 

    class Meta:
        db_table = 'bookings'


class Feedbacks(models.Model):
    feedback = models.CharField(max_length=500)
    current_date = models.DateField()

    class Meta:
        db_table = 'feedbacks'


class Messages(models.Model):
    name = models.CharField(max_length=500)
    email = models.CharField(max_length=100)
    message = models.CharField(max_length=500)

    class Meta:
        db_table = 'messages'