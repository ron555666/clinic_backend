# appointments/admin.py
from django.contrib import admin
from .models import Patient, Doctor, Appointment  # ← 关键：把三个模型都从当前 app 导入

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "phone", "email")
    search_fields = ("name", "phone", "email")

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "specialty")
    search_fields = ("name", "specialty")

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ("id", "patient", "doctor", "appointment_date", "appointment_time", "created_at")
    list_filter = ("appointment_date", "doctor")
    search_fields = ("patient__name", "doctor__name")
