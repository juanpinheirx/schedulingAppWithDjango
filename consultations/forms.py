from django import forms
from .models import Doctor

class ConsultationForm(forms.Form):
    patient_name = forms.CharField(max_length=100, label='Patient Name')
    doctor = forms.ModelChoiceField(queryset=Doctor.objects.all(), label='Doctor')
    appointment_date = forms.DateField(label='Appointment Date')
    appointment_time = forms.TimeField(label='Appointment Time')
