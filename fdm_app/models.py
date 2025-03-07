from django.db import models

# Create your models here.

class Technician(models.Model):
    technician_id = models.CharField(
        max_length=50,
        primary_key=True,
        help_text='id du technicien'
    )
    first_name = models.CharField(
        max_length=50,
        help_text='nom du technicien'
    )
    last_name = models.CharField(
        max_length=50,
        help_text='prenom du technicien'
    )
    
    

class Mission(models.Model):
    mission_id = models.CharField(
        max_length=15,
        primary_key=True,
        help_text='id de la mission'
    )
    
    mission_details = models.TextField(
        help_text='details de la mission',
        verbose_name='Mission Details'
    )
    
    start_date = models.DateField(
        help_text='date de debut de la mission',
        verbose_name='Start Date'
    )
    start_hour = models.TimeField(
        help_text='heure de debut de la mission',
        verbose_name='Start Hour'
    )
    end_date = models.DateField(
        help_text='date de fin de la mission',
        verbose_name='End Date'
    )
    end_hour = models.TimeField(
        help_text='heure de fin de la mission',
        verbose_name='End Hour'
    )
    technician = models.ForeignKey(
        Technician,
        on_delete=models.CASCADE,
        help_text='technicien de la mission'
    )
    location = models.CharField(
        max_length=50,
        help_text='lieu de la mission'
    )
    
    facturation = models.BooleanField(
        help_text='facturation de la mission, facturee ou non',
        verbose_name='Facturation'
    )
    
    
    
    
class Expense(models.Model):
    hosting = models.CharField(
        max_length=100,
        help_text='hebergement'
    )
    
    meal = models.CharField(
        max_length=100,
        help_text='repas'
    )
    
    transport = models.CharField(
        max_length=100,
        help_text='transport'
    )
    
    various_expenses = models.CharField(
        max_length=100,
        help_text='divers frais'
    )
 
    

    
    
    
    
    
    

    
    


    