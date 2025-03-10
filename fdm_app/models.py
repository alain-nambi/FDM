from django.db import models

# Create your models here.

class Technician(models.Model):
   
    first_name = models.CharField(
        max_length=50,
        help_text='nom du technicien'
    )
    last_name = models.CharField(
        max_length=50,
        help_text='prenom du technicien'
    )
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    

class Mission(models.Model):
    
    
    techniciens = models.ManyToManyField(Technician, related_name="missions")
   
    
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
    
    location = models.CharField(
        max_length=50,
        help_text='lieu de la mission'
    )
    
    facturation = models.BooleanField(
        help_text='facturation de la mission, facturee ou non',
        verbose_name='Facturation'
    )
    
    
   
    
class Expense(models.Model):
    
    
    mission = models.ForeignKey(Mission, on_delete=models.CASCADE, related_name="depenses")
    
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
    def __str__(self):
        return f"{self.hosting}Ar, {self.meal}, {self.transport}, {self.various_expenses}Ar"
        
   
    
    


    
    
    
    
    
    

    
    


    