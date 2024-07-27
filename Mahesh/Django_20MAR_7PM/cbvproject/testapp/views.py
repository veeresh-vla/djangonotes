from django.shortcuts import render
from django.views.generic import View,TemplateView
from django.http import HttpResponse
# Create your views here.
class HelloWorldView(View):
    def get(self,request):
        return HttpResponse('<h1>This response is from class based view</h1>')

class TemplateCBV(TemplateView):
    template_name = 'testapp/results.html'

class TemplateCBV2(TemplateView):
    template_name = 'testapp/results2.html'
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'Radhika'
        context['marks'] = 98
        context['subject'] = 'Python'
        return context
