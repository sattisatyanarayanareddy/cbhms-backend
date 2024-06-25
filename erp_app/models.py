from django.db import models

# Create your models here.
class Doctors_Details(models.Model):
    name = models.CharField(max_length = 100)
    email = models.CharField(max_length = 150,null=True)
    username = models.CharField(max_length = 150,null=True)
    password = models.CharField(max_length = 150,null=True)
    mobile = models.CharField(max_length = 150,null=True)
    age = models.IntegerField()
    languages = models.CharField(max_length=200,null=True)
    gender = models.CharField(max_length = 100)
    profile_path = models.CharField(max_length =150,null=True)

    