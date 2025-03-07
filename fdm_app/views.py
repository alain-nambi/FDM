from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, FormView, View
# Create your views here.
class HomeView(TemplateView):
    template_name = 'index.html'