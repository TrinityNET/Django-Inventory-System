from django import forms
from .models import Equipment

class EquipmentFilterForm(forms.Form):
    quantity = forms.IntegerField(required=True)
    audit = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))
    equipment_type = forms.ChoiceField(choices=Equipment.EQUIPMENT_TYPES, required=False)
    location = forms.ChoiceField(choices=Equipment.LOCATIONS, required=False)