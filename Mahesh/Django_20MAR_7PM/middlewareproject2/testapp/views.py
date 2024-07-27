from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home_page_view(request):
    print('This line printed by view function')
    return HttpResponse('<h1>This is from view function</h1>')
