from django.db import models
from patients.models import Patient

# Create your models here.

# Hospital Resource Management 

# Resources 

# Doctors class where each doctor has a name, a specialization, and a phone number and their assigned patients from patients app

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    # Assigned patients from patients app check assingned doctor to patient, if not assigned, return None, if assigned, return doctor name create list of patients
    
    def assigned_patients(self):
        return list(Patient.objects.filter(assigned_doctor=self))
    
    
    patientsassigned = property(assigned_patients)

     




    
    
    def __str__(self):
        return self.name

# Nurses class where each nurse has a name, a specialization, and a phone number and their assigned ward in the hospital, with ward number and number of beds

class Nurse(models.Model):
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    ward = models.ForeignKey('Ward', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name

# Ward class where each ward has a number and a number of beds and details about assignments of beds, based on bed assigned to patient in patients app



class Ward(models.Model):
    number = models.IntegerField()
    number_of_beds = models.IntegerField()
    # Assigned beds from patients app check assingned bed to patient, if not assigned, return None, if assigned, return bed number create list of patients, user get to choose bed number from list of beds in ward, each ward has 15 beds
    def assigned_beds(self):
        return list(Patient.objects.filter(assigned_ward=self))
    # Get list of nurses assigned to ward
    def assigned_nurses(self):
        return list(Nurse.objects.filter(ward=self))
        


    

    
    

    bedsassigned = property(assigned_beds)
    






    def __str__(self):
        return str(self.number)

