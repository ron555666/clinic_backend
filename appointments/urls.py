from .views import (
    home,
    appointment_create_html,
    patient_create_html,
    PatientViewSet,
    DoctorViewSet,
    AppointmentViewSet,
)
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'patients', PatientViewSet)
router.register(r'doctors', DoctorViewSet)
router.register(r'appointments', AppointmentViewSet)

urlpatterns = [
    path('', home, name='home'),
    path('api/', include(router.urls)),
    path('make/', appointment_create_html, name='make_appointment_page'),
    path('patients/create/', patient_create_html, name='create_patient')
]
