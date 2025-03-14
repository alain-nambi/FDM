from django.shortcuts import render, redirect
from django.views.generic import ListView, FormView
from django.urls import reverse_lazy
from .models import Mission, Expense,Technician
from django.views import View
from decimal import Decimal
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.db.models.functions import TruncMonth,ExtractMonth,ExtractYear
from django.utils.dateparse import parse_date
from datetime import datetime
import calendar
import re

class MissionListView(View):
    
    #obtenir la liste nécessaire pour afficher les missions et les techniciens            
    #rechercher les missions
    def get(self, request, *args, **kwargs):
        # Récupérer toutes les missions
        all_missions = Mission.objects.all().order_by('-id')
        # Filtrer les missions en fonction de la recherche
        search_query = request.GET.get('search', '')
        if search_query:
            mois_fr = {
                'janvier': 1, 'février': 2, 'mars': 3, 'avril': 4, 'mai': 5, 'juin': 6,
                'juillet': 7, 'août': 8, 'septembre': 9, 'octobre': 10, 'novembre': 11, 'décembre': 12
            }
            search_lower = search_query.lower()
            month_number = None
            for month_name, month_num in mois_fr.items():
                if month_name.startswith(search_lower):
                    month_number = month_num
                    break
            
            # Vérifier si c'est une année
            is_year = search_query.isdigit() and len(search_query) == 4
            
            if month_number and is_year:
                # Si la recherche contient un mois et une année
                all_missions = all_missions.filter(
                    Q(start_date__month=month_number, start_date__year=search_query) |
                    Q(end_date__month=month_number, end_date__year=search_query)
                )
            elif month_number:
                # Si la recherche est seulement un mois
                all_missions = all_missions.filter(
                    Q(start_date__month=month_number) |
                    Q(end_date__month=month_number)
                )
            elif is_year:
                # Si la recherche est seulement une année
                all_missions = all_missions.filter(
                    Q(start_date__year=search_query) |
                    Q(end_date__year=search_query)
                )
            else:
                
                # Recherche standard
                search_terms = search_query.split(' ')
                if len(search_terms) == 1:
                    all_missions = all_missions.filter(
                        Q(id__icontains=search_query) |
                        Q(mission_details__icontains=search_query) |
                        Q(location__icontains=search_query) |
                        Q(techniciens__first_name__icontains=search_query) |
                        Q(techniciens__last_name__icontains=search_query)
                        
                    ).distinct()
                else:
                    all_missions = all_missions.filter(
                        Q(id__icontains=search_query) |
                        Q(location__icontains=search_query) |
                        Q(mission_details__icontains=search_query) |
                 (
                 (Q(techniciens__first_name__icontains=search_terms[0]) & Q(techniciens__last_name__icontains=search_terms[1])) |
                 (Q(techniciens__first_name__icontains=search_terms[1]) & Q(techniciens__last_name__icontains=search_terms[0]))
                 )
                       ).distinct()
                    
                    
      #pagination 
        paginator = Paginator(all_missions, 10)
        page = request.GET.get('page',1)
        try:
            missions = paginator.page(page)
        except PageNotAnInteger:
            missions = paginator.page(1)
        except EmptyPage:
            missions = paginator.page(paginator.num_pages)
        #recupere les techniciens pour le formulaire
        technicians = Technician.objects.all()
        
        context = {
            'missions': missions,
            'technicians': technicians
        }
        return render(request, 'index.html', context)
        
#stockage des données de la mission dans la base 
    def post(self, request, *args, **kwargs):
        mission_details = request.POST.get('mission_details')
        start_date = request.POST.get('start_date')
        start_hour = request.POST.get('start_hour')
        end_date = request.POST.get('end_date')
        end_hour = request.POST.get('end_hour')
        location = request.POST.get('location')
        facturation = request.POST.get('facturation') == 'on'
        hosting_days = int(request.POST.get('hosting_days', 0))
        overnight_rate = Decimal(request.POST.get('overnight_rate' , 0))
        meal_costs = Decimal(request.POST.get('meal_costs', 0))
        transport = request.POST.get('transport')
        shipping_costs = Decimal(request.POST.get('shipping_costs', 0))
        various_expenses_details = request.POST.get('various_expenses_details')
        various_expenses_price = Decimal(request.POST.get('various_expenses_price',0))
        
        # Créer une nouvelle mission avec les données récupérées
        mission = Mission.objects.create(
            mission_details=mission_details,
            start_date=start_date,
            start_hour=start_hour,
            end_date=end_date,
            end_hour=end_hour,
            location=location,
            facturation=facturation
        )
        techniciens_ids = request.POST.getlist('techniciens')
        for tech_id in techniciens_ids:
            technician = Technician.objects.get(id=tech_id)
            mission.techniciens.add(technician)

    # Créer une nouvelle dépense associée à la mission
        Expense.objects.create(
            mission=mission,
            hosting_days=hosting_days,
            overnight_rate=overnight_rate,
            meal_costs=meal_costs,
            transport=transport,
            shipping_costs=shipping_costs,
            various_expenses_details=various_expenses_details,
            various_expenses_price=various_expenses_price
        )
        
        return redirect('missions')
    
    

    
   


    
    
    
  
   
