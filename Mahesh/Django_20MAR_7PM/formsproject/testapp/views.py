from django.shortcuts import render
from testapp.forms import StudentForm
# Create your views here.
def studentinput_view(request):
    submitted = False
    sname = ''
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            print('Form validation success and print data')
            print('Name:',form.cleaned_data['name'])
            print('RollNo:',form.cleaned_data['rollno'])
            print('Marks:',form.cleaned_data['marks'])
            submitted = True
            sname = form.cleaned_data['name']
    form = StudentForm()
    return render(request,'testapp/input.html', {'form':form,'submitted':submitted,'sname':sname})
