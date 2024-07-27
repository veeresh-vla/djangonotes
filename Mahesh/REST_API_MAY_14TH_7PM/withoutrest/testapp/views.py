from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def emp_data_view(request):
    emp_data = {
    'eno':101,
    'ename':'Sunny',
    'esal':12000,
    'eaddr':'Mumbai'
    }
    resp ='<h1>Employee Number:{}<br>Employee Name:{}<br>Employee Salary:{}<br>Employee Address:{}</h1>'.format(emp_data['eno'],emp_data['ename'],emp_data['esal'],emp_data['eaddr'])
    return HttpResponse(resp)

import json
def emp_data_jsonview(request):
    emp_data = {
    'eno':101,
    'ename':'Radhika',
    'esal':13000,
    'eaddr':'Vja'
    }
    json_data = json.dumps(emp_data)
    return HttpResponse(json_data,content_type='application/json')

from django.http import JsonResponse
def emp_data_jsonview2(request):
    emp_data = {
    'eno':101,
    'ename':'Lilly',
    'esal':14000,
    'eaddr':'Hyd'
    }
    return JsonResponse(emp_data)

from django.views.generic import View
from testapp.mixins import HttpResponseMixin
class JsonCBV(HttpResponseMixin,View):
    def get(self,request,*args,**kwargs):
        json_data = json.dumps({'msg':'This is from GET method'})
        return self.render_to_http_response(json_data)
    def post(self,request,*args,**kwargs):
        json_data = json.dumps({'msg':'This is from POST method'})
        return self.render_to_http_response(json_data)
    def put(self,request,*args,**kwargs):
        json_data = json.dumps({'msg':'This is from PUT method'})
        return self.render_to_http_response(json_data)
    def delete(self,request,*args,**kwargs):
        json_data = json.dumps({'msg':'This is from DELETE method'})
        return self.render_to_http_response(json_data)
