from django import forms
from .models import Equipment, Reservation

class EquipmentFilterForm(forms.Form):
    audit = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))
    equipment_type = forms.ChoiceField(choices=Equipment.EQUIPMENT_TYPES, required=False)
    location = forms.ChoiceField(choices=Equipment.LOCATIONS, required=False)

class ReservationForm(forms.Form):
    end_date = forms.DateField(required=True, widget=forms.DateInput(attrs={'type': 'date'}))