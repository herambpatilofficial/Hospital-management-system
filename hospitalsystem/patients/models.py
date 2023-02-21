from django.db import models
import datetime

# Create your models here.


class Patient(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    phone_number = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    med_history = models.TextField()
    blood_type = models.CharField(max_length=50)
    assigned_ward = models.ForeignKey('hospital.Ward', on_delete=models.SET_NULL, null=True, blank=True)
    assigned_bed = models.IntegerField(null=True, blank=True)

    # Calculate age from date_of_birth using lambda function
    age = property(lambda self: (datetime.date.today() - self.date_of_birth).days / 365)

    # Assigned Doctor from hospital app check assingned doctor to patient, if not assigned, return None, if assigned, return doctor name
    assigned_doctor = models.ForeignKey('hospital.Doctor', on_delete=models.SET_NULL, null=True, blank=True)


    def __str__(self):
        return self.first_name + " " + self.last_name + " " + str(int(self.age)) + " BED NO." + str(self.assigned_bed) + " Ward No." + str(self.assigned_ward)
    
    # Add Filter Widget
    class Meta:
        ordering = ["last_name", "first_name", "date_of_birth", "city", "blood_type"]
        verbose_name_plural = "Patients"












