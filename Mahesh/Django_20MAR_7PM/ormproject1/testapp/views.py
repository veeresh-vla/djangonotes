from django.shortcuts import render
from testapp.models import Employee
from django.db.models import Q
from django.db.models import Avg,Max,Min,Sum,Count
# Create your views here.
def aggregate_view(request):
    print(request.user)
    avg = Employee.objects.all().aggregate(Avg('esal'))
    max = Employee.objects.all().aggregate(Max('esal'))
    min = Employee.objects.all().aggregate(Min('esal'))
    sum = Employee.objects.all().aggregate(Sum('esal'))
    count = Employee.objects.all().aggregate(Count('esal'))
    my_dict = {'avg':avg['esal__avg'], 'max':max['esal__max'], 'min':min['esal__min'],'sum':sum['esal__sum'], 'count':count['esal__count']}
    return render(request,'testapp/aggregate.html',my_dict)
from django.db.models.functions import Lower
def retrieve_view(request):
    q1 = Employee.objects.filter(esal__lte=11000)
    q2 = Employee.objects.filter(ename__startswith='S')
    q3 = q1.union(q2)
    emp_list = q3
    #emp_list = Employee.objects.all().order_by(Lower('ename'))
    return render(request,'testapp/index.html',{'emp_list':emp_list})
    #emp_list= Employee.objects.filter(esal__lte=12000)
    #emp_list = Employee.objects.filter(ename__contains='donna')
    #emp_list = Employee.objects.filter(id__in=[1,51,52])
    #emp_list = Employee.objects.filter(ename__startswith='a')
    #emp_list = Employee.objects.filter(ename__endswith='s')
    #emp_list = Employee.objects.filter(esal__range=[12000,15000])
    #emp_list = Employee.objects.filter(ename__startswith='A') | Employee.objects.filter(esal__lte=11000)
    #emp_list = Employee.objects.filter(Q(ename__startswith='A') | Q(esal__lte=11000))
    #emp_list = Employee.objects.filter(ename__startswith='S',esal__lt=18000)
    #emp_list = Employee.objects.exclude(ename__startswith='S')
    #emp_list = Employee.objects.filter(~Q(ename__startswith='D'))
    #emp_list = Employee.objects.all().values_list('ename','esal')
    #emp_list = Employee.objects.all().values('ename','esal')
    # emp_list = Employee.objects.all().only('ename','esal')
    # return render(request,'testapp/specificcolumns.html', {'emp_list':emp_list})
