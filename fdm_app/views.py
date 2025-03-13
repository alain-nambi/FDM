from django.shortcuts import render, redirect
from django.views.generic import ListView, FormView
from django.urls import reverse_lazy
from .models import Mission, Expense,Technician
from django.views import View
from decimal import Decimal
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

class MissionListView(View):
    #obtenir la liste nécessaire pour afficher les missions et les techniciens
    #pagination de la liste
    def get(self, request, *args, **kwargs):
        # Récupérer toutes les missions
        all_missions = Mission.objects.all().order_by('-id')
        paginator = Paginator(all_missions, 5)
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
    
    

    
   


    
    
    
  
   
