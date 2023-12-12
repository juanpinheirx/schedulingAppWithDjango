from django.db import models

class Doctor(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        app_label = 'consultations'

class Appointment(models.Model):
    patient_name = models.CharField(max_length=100)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    appointment_date = models.DateField()
    appointment_time = models.TimeField()

    class Meta:
        app_label = 'consultations'