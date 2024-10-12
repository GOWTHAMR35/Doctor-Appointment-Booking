from django.db import models

# Create your models here.
class DoctorDetails(models.Model):
 
    # fields of the model
    doctorName = models.CharField(max_length = 200)
    doctorDegree = models.CharField(max_length = 200)
    def __str__(self):
        return self.doctorName
class appointmentDetails(models.Model):
    appDate = models.CharField(max_length = 200)
    appTime = models.CharField(max_length = 200)
    patName = models.CharField(max_length = 200)
    def __str__(self):
        return self.appDate

    