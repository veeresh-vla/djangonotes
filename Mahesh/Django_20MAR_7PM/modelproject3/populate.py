import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'modelproject3.settings')
import django
django.setup()

from testapp.models import Student
from faker import Faker
from random import *
def phonenumbergen():
	d1 = randint(6,9)
	num = '' + str(d1)
	for i in range(9):
		num += str(randint(0,9))
	return int(num)
def populate(n):
    for i in range(n):
        fake = Faker()
        frollno = fake.random_int(min=1,max=999)
        fname = fake.name()
        fdob = fake.date()
        fmarks = fake.random_int(min=1,max=100)
        femail = fake.email()
        fphonenumber = phonenumbergen()
        faddress = fake.address()
        Student.objects.get_or_create(rollno=frollno,name=fname,dob=fdob,marks=fmarks,email=femail,phonenumber=fphonenumber,address=faddress)
n = int(input('Enter number of records:'))
populate(n)
print(f'{n} Records Inserted Successfully.....')
