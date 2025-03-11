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
    
    hosting_days = models.IntegerField(
        help_text='nombre de jours de sejour',
        default=0.0,
    )
    
    overnight_rate = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0.00,
        help_text='tarif nuitée'
       
    )
    
    total_hosting = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        help_text=' pris total de séjour',
        editable = False 
    )

    
    meal_costs = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        help_text='prix des repas',
    )
    
    total_meal_costs = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        help_text='prix total des repas',
        editable = False,
        default=0.00,
    )
    
    
    transport = models.CharField(
        max_length=100,
        help_text='transport',
    )
    
    shipping_costs = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        help_text='frais de transport',
    )
    
    various_expenses_details = models.CharField(
        max_length=100,
        help_text='divers frais',
    )
    
    various_expenses_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        help_text='prix des divers frais',
    )
    
    total_expenses = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        help_text='prix total des frais',
        editable = False,
        default=0.00,
    )
    
    def save(self, *args, **kwargs):
        # Calcul automatique du total_hosting = hosting_days * overnight_rate
        self.total_hosting = self.hosting_days * self.overnight_rate
        
        #calcul du total_meal_costs = hosting_days * meal_costs
        self.total_meal_costs = self.hosting_days * self.meal_costs
         
        #calcul des total_expenses = total_hosting + total_meal_costs + shipping_costs + various_expenses_price
        self.total_expenses = self.total_hosting + self.total_meal_costs + self.shipping_costs + self.various_expenses_price
        super().save(*args, **kwargs)
    
    
    def __str__(self):
        return f"{self.total_expenses}"
        
   
    
    


    
    
    
    
    
    

    
    


    
    


    
    
    
    
    
    

    
    


    