from .views import (
    home,
    appointment_create_html,
    patient_create_html,
    appointment_list_html,
    PatientViewSet,
    DoctorViewSet,
    AppointmentViewSet,
)
from django.urls import path, include
from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register(r'patients', PatientViewSet)
# router.register(r'doctors', DoctorViewSet)
# router.register(r'appointments', AppointmentViewSet)

# urlpatterns = [
#     path('', home, name='home'),
#     path('', include(router.urls)),  # ✅ 
#     path('make/', appointment_create_html, name='make_appointment_page'),
#     path('patients/create/', patient_create_html, name='create_patient'),
#     path('appointments/list/', appointment_list_html, name='appointment_list'),
# ]

router = DefaultRouter()
router.register(r'patients', PatientViewSet, basename='patient')
router.register(r'doctors', DoctorViewSet, basename='doctor')
router.register(r'appointments', AppointmentViewSet, basename='appointment')

urlpatterns = [
    # HTML pages
    path('', home, name='home'),
    path('make/', appointment_create_html, name='make_appointment_page'),
    path('patients/create/', patient_create_html, name='create_patient'),
    path('appointments/list/', appointment_list_html, name='appointment_list'),

    # API endpoints -> /api/patients/ /api/doctors/ /api/appointments/
    path('api/', include(router.urls)),
]