from django.shortcuts import render
from django.views.generic import View
from testapp.models import Employee
from testapp.mixins import SerializeMixin
import json
from testapp.mixins import HttpResponseMixin
from testapp.utils import is_json
from testapp.forms import EmployeeForm
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
@method_decorator(csrf_exempt,name='dispatch')
class EmployeeCRUDCBV(HttpResponseMixin,SerializeMixin,View):
    def get_object_by_id(self,id):
        try:
            emp = Employee.objects.get(id=id)
        except Employee.DoesNotExist:
            emp = None
        return emp
    def get(self,request,*args,**kwargs):
        data = request.body
        valid_json = is_json(data)
        if not valid_json:
            json_data = json.dumps({'msg':'Please send valid data only'})
            return self.render_to_http_response(json_data,status=400)
        pdata = json.loads(data)
        id = pdata.get('id',None)
        if id is not None:
            emp = self.get_object_by_id(id=id)
            if emp is None:
                json_data = json.dumps({'msg':'The requested resource not available with matched id'})
                return self.render_to_http_response(json_data,status=404)
            json_data = self.serialize([emp])
            return self.render_to_http_response(json_data)
        qs = Employee.objects.all()
        json_data = self.serialize(qs)
        return self.render_to_http_response(json_data)

    def post(self,request,*args,**kwargs):
        data = request.body
        valid_json = is_json(data)
        if not valid_json:
            json_data = json.dumps({'msg':'Please send valid data only'})
            return self.render_to_http_response(json_data,status=400)
        empdata = json.loads(data)
        form = EmployeeForm(empdata)
        if form.is_valid():
            form.save(commit = True)
            json_data = json.dumps({'msg':'Resource created successfully...'})
            return self.render_to_http_response(json_data)
        if form.errors:
            json_data = json.dumps(form.errors)
            return self.render_to_http_response(json_data,status=400)

    def put(self,request,*args,**kwargs):
        data = request.body
        valid_json = is_json(data)
        if not valid_json:
            json_data = json.dumps({'msg':'Please send valid data only'})
            return self.render_to_http_response(json_data,status=400)
        pdata = json.loads(data)
        id = pdata.get('id',None)
        if id is None:
            json_data = json.dumps({'msg':'To perform updation id is mandatory, please provide'})
            return self.render_to_http_response(json_data,status=404)
        emp = self.get_object_by_id(id=id)
        if emp is None:
            json_data = json.dumps({'msg':'No resource with matched id, not possible to perform updation'})
            return self.render_to_http_response(json_data,status=404)
        provided_data = json.loads(data)
        original_data = {
        'eno':emp.eno,
        'ename':emp.ename,
        'esal':emp.esal,
        'eaddr':emp.eaddr,
        }
        original_data.update(provided_data)
        form = EmployeeForm(original_data,instance=emp)
        if form.is_valid():
            form.save(commit = True)
            json_data = json.dumps({'msg':'Resource updated successfully...'})
            return self.render_to_http_response(json_data)
        if form.errors:
            json_data = json.dumps(form.errors)
            return self.render_to_http_response(json_data,status=400)

    def delete(self,request,*args,**kwargs):
        data = request.body
        valid_json = is_json(data)
        if not valid_json:
            json_data = json.dumps({'msg':'Please send valid data only'})
            return self.render_to_http_response(json_data,status=400)
        padat = json.loads(data)
        id = padat.get('id',None)
        if id is not None:
            emp = self.get_object_by_id(id)
            if emp is None:
                json_data = json.dumps({'msg':'The requested resource not available with matched id'})
                return self.render_to_http_response(json_data,status=404)
            status,deleted_item = emp.delete()
            if status == 1:
                json_data = json.dumps({'msg':'Resource deleted successfully...'})
                return self.render_to_http_response(json_data)
            json_data = json.dumps({'msg':'Unable to delete...pls try again...'})
            return self.render_to_http_response(json_data)
        json_data = json.dumps({'msg':'To perform deletion id is mandatory'})
        return self.render_to_http_response(json_data,status=404)













@method_decorator(csrf_exempt,name='dispatch')
class EmployeeDetailCBV(HttpResponseMixin,SerializeMixin,View):
    def get_object_by_id(self,id):
        try:
            emp = Employee.objects.get(id=id)
        except Employee.DoesNotExist:
            emp = None
        return emp
    def put(self,request,id,*args,**kwargs):
        emp = self.get_object_by_id(id)
        if emp is None:
            json_data = json.dumps({'msg':'No matched resource found, not possible to perform updation'})
            return self.render_to_http_response(json_data,status=404)
        data = request.body
        valid_json = is_json(data)
        if not valid_json:
            json_data = json.dumps({'msg':'Please send valid data only'})
            return self.render_to_http_response(json_data,status=400)
        provided_data = json.loads(data)
        original_data = {
        'eno':emp.eno,
        'ename':emp.ename,
        'esal':emp.esal,
        'eaddr':emp.eaddr
        }
        original_data.update(provided_data)
        form = EmployeeForm(original_data,instance=emp)
        if form.is_valid():
            form.save(commit = True)
            json_data = json.dumps({'msg':'Resource updated successfully...'})
            return self.render_to_http_response(json_data)
        if form.errors:
            json_data = json.dumps(form.errors)
            return self.render_to_http_response(json_data,status=400)

    def delete(self,request,id,*args,**kwargs):
        emp = self.get_object_by_id(id)
        if emp is None:
            json_data = json.dumps({'msg':'No matched resource found, not possible to perform deletion'})
            return self.render_to_http_response(json_data,status=404)
        #t = emp.delete() #The return type of delete() is tuple
        status, deleted_item = emp.delete()
        if status == 1:
            json_data = json.dumps({'msg':'Resources deleted successfully'})
            return self.render_to_http_response(json_data)
        json_data = json.dumps({'msg':'Unable to delete...plz try again..'})
        return self.render_to_http_response(json_data)

    def get(self,request,id,*args,**kwargs):
        try:
            emp = Employee.objects.get(id=id)
        except Employee.DoesNotExist:
            json_data = json.dumps({'msg':'The requested resource not available'})
            return self.render_to_http_response(json_data,status=404)
        else:
            json_data = self.serialize([emp,])
            return self.render_to_http_response(json_data)

@method_decorator(csrf_exempt,name='dispatch')
class EmployeeListCBV(HttpResponseMixin,SerializeMixin,View):
    def get(self,request,*args,**kwargs):
        qs = Employee.objects.all()
        json_data = self.serialize(qs)
        return self.render_to_http_response(json_data)
    def post(self,request,*args,**kwargs):
        data = request.body
        valid_json = is_json(data)
        if not valid_json:
            json_data = json.dumps({'msg':'Please send valid data only'})
            return self.render_to_http_response(json_data,status=400)
        empdata = json.loads(data)
        form = EmployeeForm(empdata)
        if form.is_valid():
            form.save(commit = True)
            json_data = json.dumps({'msg':'Resource created successfully...'})
            return self.render_to_http_response(json_data)
        if form.errors:
            json_data = json.dumps(form.errors)
            return self.render_to_http_response(json_data,status=400)
