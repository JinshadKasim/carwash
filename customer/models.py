from django.db import models

# Create your models here.

class Users(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.BigIntegerField()
    password = models.CharField(max_length=100)

    class Meta:
        db_table = 'users'

    