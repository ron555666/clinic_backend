from django.urls import reverse_lazy
from rest_framework import viewsets
from .models import Patient, Doctor, Appointment
from .serializers import PatientSerializer, DoctorSerializer, AppointmentSerializer

from django.views.generic.edit import CreateView
from .forms import AppointmentForm, PatientForm

from django.http import HttpResponse


def home(request):
    return HttpResponse("<h1>Welcome to the Clinic Appointment System</h1><p><a href='/api/make/'>Go to Make Appointment</a></p>")
    

class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

class AppointmentCreateView(CreateView):
    model = Appointment
    form_class = AppointmentForm
    template_name = 'appointments/appointment_form.html'
    success_url = '/' 


class PatientCreateView(CreateView):
    model = Patient
    form_class = PatientForm
    template_name = 'appointments/patient_form.html'
    success_url = reverse_lazy('make_appointment')  # 提交后跳回预约页面