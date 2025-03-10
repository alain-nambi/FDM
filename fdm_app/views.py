from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, FormView, View,ListView
from .models import Mission
# Create your views here.
#class HomeView(TemplateView):
 #   template_name = 'index.html'
    
class MissionListView(ListView):
    model = Mission
    template_name = 'index.html'
    context_object_name = 'missions'
   