from django.db import models

class Patient(models.Model):
    name = models.CharField(max_length=100)
    diseases = models.TextField()
    allergies = models.TextField()
    room_number = models.IntegerField()
    bed_number = models.IntegerField()
    floor_number = models.IntegerField()
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    contact_info = models.CharField(max_length=15)
    emergency_contact = models.CharField(max_length=15)
    additional_info = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
    

class DietChart(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    morning_meal = models.TextField()
    evening_meal = models.TextField()
    night_meal = models.TextField()
    special_instructions = models.TextField()

    def __str__(self):
        return str(self.patient)
    