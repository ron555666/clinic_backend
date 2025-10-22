from django.urls import reverse_lazy
from rest_framework import viewsets
from .models import Patient, Doctor, Appointment
from .serializers import PatientSerializer, DoctorSerializer, AppointmentSerializer

from django.views.decorators.csrf import csrf_exempt

from django.http import HttpResponse
from django.shortcuts import render, redirect
from datetime import date
from django.core.paginator import Paginator
from django.utils.dateparse import parse_date


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

def appointment_list_html(request):
    q_patient = request.GET.get("patient", "").strip()
    q_doctor  = request.GET.get("doctor", "").strip()
    q_date    = request.GET.get("date", "").strip()

    qs = Appointment.objects.select_related("patient", "doctor").order_by(
        "appointment_date", "appointment_time"
    )

    if q_patient:
        qs = qs.filter(patient__name__icontains=q_patient)
    if q_doctor:
        qs = qs.filter(doctor__name__icontains=q_doctor)
    if q_date:
        d = parse_date(q_date)
        if d:
            qs = qs.filter(appointment_date=d)

    paginator = Paginator(qs, 20)
    page_obj = paginator.get_page(request.GET.get("page", 1))

    ctx = {
        "page_obj": page_obj,
        "q_patient": q_patient,
        "q_doctor": q_doctor,
        "q_date": q_date,
    }
    return render(request, "appointments/appointment_list.html", ctx)


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
