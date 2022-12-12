from django.db import models

# Create your models here.

class Admins(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    class Meta:
        db_table = 'admins'