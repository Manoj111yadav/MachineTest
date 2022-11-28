from django.db import models

# Create your models here.

class User(models.Model):
    Id = models.AutoField(primary_key=True)
    Full_Name = models.CharField(max_length=500)
    Gmail = models.CharField(max_length=500)
    Phone = models.CharField(max_length=500)
    Password = models.CharField(max_length=500)
    Project_Name = models.CharField(max_length=500)


class Cleint(models.Model):
    Client_Id = models.AutoField(primary_key=True)
    Client_Name = models.CharField(max_length=500)
    Project_Name = models.CharField(max_length=500)
   
class Project(models.Model):
    Project_Id = models.AutoField(primary_key=True)
    Project_Name = models.CharField(max_length=500)
    Cleint_Name = models.CharField(max_length=500)
