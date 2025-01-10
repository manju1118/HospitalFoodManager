from django import forms
from hospital.models import Patient,DietChart


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = "__all__"
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'diseases':forms.Textarea(attrs={'class':'form-control'}),
            'allergies':forms.Textarea(attrs={'class':'form-control'}),
            'room_number':forms.NumberInput(attrs={'class':'form-control'}),
            'bed_number':forms.NumberInput(attrs={'class':'form-control'}),
            'floor_number':forms.NumberInput(attrs={'class':'form-control'}),
            'age':forms.NumberInput(attrs={'class':'form-control'}),
            'gender':forms.TextInput(attrs={'class':'form-control'}),
            'contact_info':forms.TextInput(attrs={'class':'form-control'}),
            'emergency_contact':forms.TextInput(attrs={'class':'form-control'}),
            'additional_info':forms.Textarea(attrs={'class':'form-control'}),
        }



class DietChartForm(forms.ModelForm):
    class Meta:
        model = DietChart
        fields = '__all__'
        widgets = {
           
            'morning_meal':forms.Textarea(attrs={'class':'form-control'}),
            'evening_meal':forms.Textarea(attrs={'class':'form-control'}),
            'night_meal':forms.Textarea(attrs={'class':'form-control'}),
            'special_instructions':forms.Textarea(attrs={'class':'form-control'})
        }

