from django.urls import reverse_lazy
from rest_framework import viewsets
from .models import Patient, Doctor, Appointment
from .serializers import PatientSerializer, DoctorSerializer, AppointmentSerializer

from django.views.decorators.csrf import csrf_exempt

from django.http import HttpResponse
from django.shortcuts import render, redirect
from datetime import date


def home(request):
    return render(request, 'appointments/home.html')


def appointment_create_html(request):
    patients = Patient.objects.all()
    doctors = Doctor.objects.all()
    return render(request, 'appointments/appointment_page.html', {
        'patients': patients,
        'doctors': doctors,
        'today': date.today().strftime('%Y-%m-%d')
    })

@csrf_exempt
def patient_create_html(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        Patient.objects.create(name=name, email=email, phone=phone)
        return redirect('make_appointment_page')
    return render(request, 'appointments/create_patient.html')


#  DRF API
class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
