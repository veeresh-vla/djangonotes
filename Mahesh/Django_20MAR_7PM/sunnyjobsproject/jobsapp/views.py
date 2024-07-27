from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def hyd_jobs_view(request):
    s = '<h1>Hyderabad Jobs Information</h1>'
    return HttpResponse(s)
def bng_jobs_view(request):
    s = '<h1>Bangalore Jobs Information</h1>'
    return HttpResponse(s)
def pune_jobs_view(request):
    s = '<h1>Pune Jobs Information</h1>'
    return HttpResponse(s)
def bihar_jobs_view(request):
    s = '<h1>Bihar Jobs Information</h1>'
    return HttpResponse(s)
