from django.contrib import admin
from .models import Technician, Mission, Expense

# Register your models here.

admin.site.register(Technician)
admin.site.register(Mission)
admin.site.register(Expense)