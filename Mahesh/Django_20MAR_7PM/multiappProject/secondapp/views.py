from django.shortcuts import render
from django.http import HttpResponse
def wish2(request):
    return HttpResponse('<h1>Hello This Is From Second Application</h1>')
