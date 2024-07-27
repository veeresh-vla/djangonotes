from django.shortcuts import render
from rest_framework import generics
from testapp.models import Employee
from testapp.serializers import EmployeeSerializer
from testapp.pagination import MyPagination,MyPagination2,MyPagination3
# Create your views here.

class EmployeeListView(generics.ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    ordering_fields = ('eno','esal')
