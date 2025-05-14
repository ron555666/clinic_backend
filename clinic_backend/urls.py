from django.contrib import admin
from django.urls import path, include
from appointments.views import PatientCreateView  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'), 
    path('api/', include('appointments.urls')), 
    path('patients/create/', PatientCreateView.as_view(), name='create_patient'),
]
