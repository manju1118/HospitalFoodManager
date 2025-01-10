from django import forms
from pantry.models import PantryStaff,MealPreparation


class PantryStaffForm(forms.ModelForm):
    class Meta:
        model = PantryStaff
        fields = '__all__'
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'contact_info':forms.NumberInput(attrs={'class':'form-control'}),
            'location':forms.TextInput(attrs={'class':'form-control'}),
        }


class MealPreparationForm(forms.ModelForm):
    class Meta:
        model = MealPreparation
        fields = '__all__'
        widgets = {
            'meal_type':forms.Select(attrs={'class':'form-control'}),
            'status':forms.Select(attrs={'class':'form-control'}),
            'location':forms.TextInput(attrs={'class':'form-control'}),
        }