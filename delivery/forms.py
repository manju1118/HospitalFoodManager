from django import forms
from delivery.models import DeliveryPersonnel,MealDelivery


class DeliveryPersonnelForm(forms.ModelForm):
    class Meta:
        model = DeliveryPersonnel
        fields = '__all__'
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'contact_info':forms.TextInput(attrs={'class':'form-control'}),
            'additional_details':forms.Textarea(attrs={'class':'form-control'}),
        }


class MealDeliveryForm(forms.ModelForm):
    class Meta:
        model = MealDelivery
        fields = '__all__'
        widgets = {
            'meal_preparation':forms.Select(attrs={'class':'form-control'}),
            'delivery_person':forms.Select(attrs={'class':'form-control'}),
            'status':forms.Select(attrs={'class':'form-control'}),
            'delivered_at':forms.DateInput(attrs={'class':'form-control', 'type': 'date',}),
            'notes':forms.Textarea(attrs={'class':'form-control'}),
        }

