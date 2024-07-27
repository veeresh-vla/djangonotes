from django.shortcuts import render
import  datetime
from django.http import  HttpResponse
# Create your views here.
def time_info(request):
    date = datetime.datetime.now()
    msg = '<h1>Hello Friend Very'
    h = int(date.strftime('%H'))
    if h<12:
        msg += ' Good Morning'
    elif h<16:
        msg += ' Good Afternoon'
    elif h<21:
        msg += ' Good Evening'
    else:
        msg += ' Good Night'
    msg += '</h1><hr>'
    msg += '<h1>Now server time is:'+str(date)+'</h1>'
    return HttpResponse(msg)


