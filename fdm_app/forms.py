# frais_de_mission/fdm_app/forms.py
from django import forms
from .models import Mission, Technician

class MissionForm(forms.ModelForm):
    class Meta:
        model = Mission
        fields = ['location', 'techniciens', 'mission_details', 'start_date', 'start_hour', 'end_date', 'end_hour', 'facturation']
        widgets = {
            'techniciens': forms.CheckboxSelectMultiple(),
        }