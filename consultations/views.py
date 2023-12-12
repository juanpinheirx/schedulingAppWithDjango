from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponseBadRequest
from .models import Doctor, Appointment
from .forms import ConsultationForm

class ScheduleConsultationView(View):
    template_name = 'consultations/schedule_consultation.html'

    def get(self, request):
        form = ConsultationForm()
        doctors = Doctor.objects.all()
        return render(request, self.template_name, {'form': form, 'doctors': doctors})

    def post(self, request):
        form = ConsultationForm(request.POST)

        if form.is_valid():
            doctor = form.cleaned_data['doctor']
            appointment_date = form.cleaned_data['appointment_date']
            appointment_time = form.cleaned_data['appointment_time']

            existing_appointment = Appointment.objects.filter(
                doctor=doctor,
                appointment_date=appointment_date,
                appointment_time=appointment_time,
            ).first()

            if existing_appointment:
                return HttpResponseBadRequest('Horário indisponível (já marcado com este médico)')

            Appointment.objects.create(
                patient_name=form.cleaned_data['patient_name'],
                doctor=doctor,
                appointment_date=appointment_date,
                appointment_time=appointment_time,
            )

            return redirect('success_page')

        doctors = Doctor.objects.all()
        return render(request, self.template_name, {'form': form, 'doctors': doctors})

class SuccessPageView(View):
    template_name = 'consultations/success_page.html'

    def get(self, request):
        return render(request, self.template_name)