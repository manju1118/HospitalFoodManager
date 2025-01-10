from django.db import models
from hospital.models import Patient

class PantryStaff(models.Model):
    name = models.CharField(max_length=100)
    contact_info = models.CharField(max_length=15)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class MealPreparation(models.Model):
    patient = models.ForeignKey('hospital.Patient', on_delete=models.CASCADE)
    meal_type = models.CharField(max_length=10, choices=[('Morning', 'Morning'), ('Evening', 'Evening'), ('Night', 'Night')])
    status = models.CharField(max_length=15, choices=[('Pending', 'Pending'), ('Prepared', 'Prepared')], default='Pending')
    prepared_by = models.ForeignKey(PantryStaff, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return str(self.prepared_by)