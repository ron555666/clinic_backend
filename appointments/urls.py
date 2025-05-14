from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    home,
    PatientViewSet,
    DoctorViewSet,
    AppointmentViewSet,
    AppointmentCreateView,
    PatientCreateView,  # ✅ 一定要导入
)

router = DefaultRouter()
router.register(r'patients', PatientViewSet)
router.register(r'doctors', DoctorViewSet)
router.register(r'appointments', AppointmentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('', home, name='home'),
    
    path('make/', AppointmentCreateView.as_view(), name='make_appointment'),
]
