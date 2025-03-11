from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, FormView, View,ListView
from .models import Mission
from .forms import MissionForm
from django.urls import reverse_lazy

# Create your views here.
#class HomeView(TemplateView):
 #   template_name = 'index.html'
    
    
    #retourne les missions
class MissionListView(ListView):
    model = Mission
    template_name = 'index.html'
    context_object_name = 'missions'
    
    def get_queryset(self):
        #return Mission.objects.filter(facturation=True)
        return Mission.objects.all()
    
   
