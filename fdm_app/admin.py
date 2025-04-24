from django.contrib import admin
from .models import Technician, Mission, Expense , MissionFile

# Register your models here.

admin.site.register(Technician)
admin.site.register(Mission)
admin.site.register(Expense)
admin.site.register(MissionFile)