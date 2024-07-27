from django.db import models

# Create your models here.
class ContactInfo(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    address = models.CharField(max_length=30)
    class Meta:
        abstract = True
class Student(ContactInfo):
    rollno = models.IntegerField()
    marks = models.IntegerField()
class Teacher(ContactInfo):
    subject = models.CharField(max_length=30)
    salary = models.FloatField()

class ContactInfo1(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    address = models.CharField(max_length=30)
class Student1(ContactInfo1):
    rollno = models.IntegerField()
    marks = models.IntegerField()
class Teacher1(ContactInfo1):
    subject = models.CharField(max_length=30)
    salary = models.FloatField()

class Person(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
class Employee(Person):
    eno = models.IntegerField()
    esal = models.FloatField()
class Manager(Employee):
    exp = models.IntegerField()
    team_size = models.IntegerField()

class Parent1(models.Model):
    f1 = models.CharField(max_length=30)
    f2 = models.CharField(max_length=30)
class Parent2(models.Model):
    f3 = models.CharField(max_length=30,primary_key=True)
    f4 = models.CharField(max_length=30)
class Child(Parent1,Parent2):
    f5 = models.CharField(max_length=30)
    f6 = models.CharField(max_length=30)
