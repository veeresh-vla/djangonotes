from django.db import models

# Create your models here.
class Employee(models.Model):
    eno = models.IntegerField()
    ename = models.CharField(max_length=30)
    esal = models.FloatField()
    eadddr = models.CharField(max_length=30)