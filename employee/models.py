from django.db import models

# Create your models here.


class Employees(models.Model):
    emp_name = models.CharField(max_length=100)
    emp_phone = models.BigIntegerField()
    emp_email = models.CharField(max_length=100)
    emp_dob = models.DateField()
    emp_address = models.CharField(max_length=100)
    emp_idproof = models.CharField(max_length=100)
    emp_idproofnum = models.BigIntegerField()
    emp_photo = models.ImageField(upload_to="profile_images")
    emp_password = models.CharField(max_length=100)


    class Meta:
        db_table = 'employees'