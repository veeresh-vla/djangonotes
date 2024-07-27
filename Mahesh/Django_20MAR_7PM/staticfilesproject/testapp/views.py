from django.shortcuts import render

# Create your views here.
def result_view(request):
    subjects = {'s1':'Python','s2':'Django','s3':'RestAPI','s4':'MongoDB'}
    return render(request,'testapp/results.html',subjects)
