from django.urls import path
from .views import ScheduleConsultationView
from consultations.views import SuccessPageView

urlpatterns = [
    path('schedule/', ScheduleConsultationView.as_view(), name='schedule_consultation'),
    path('success/', SuccessPageView.as_view(), name='success_page'),

]
