from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from testapp.models import Company
# Create your views here.
class CompanyListView(ListView):
    model = Company

class CompanyDetailView(DetailView):
    model = Company

class CompanyCreateView(CreateView):
    model = Company
    fields = '__all__'

class CompanyUpdateView(UpdateView):
    model = Company
    fields = ('location','ceo')

from django.urls import reverse_lazy
class CompanyDeleteView(DeleteView):
    model = Company
    success_url = reverse_lazy('list')
