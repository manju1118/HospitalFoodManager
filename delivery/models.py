from django.db import models
from pantry.models import MealPreparation
from hospital.models import Patient

class DeliveryPersonnel(models.Model):
    name = models.CharField(max_length=100)
    contact_info = models.CharField(max_length=15)
    additional_details = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
    

class MealDelivery(models.Model):
    meal_preparation = models.ForeignKey('pantry.MealPreparation', on_delete=models.CASCADE)
    delivery_person = models.ForeignKey(DeliveryPersonnel, on_delete=models.SET_NULL, null=True)
    status = models.CharField(max_length=15, choices=[('Pending', 'Pending'), ('Delivered', 'Delivered')], default='Pending')
    delivered_at = models.DateTimeField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.delivery_person)
