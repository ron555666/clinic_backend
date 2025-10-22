# appointments/management/commands/seed_demo.py
from django.core.management.base import BaseCommand
from datetime import date, time, timedelta
from appointments.models import Patient, Doctor, Appointment

class Command(BaseCommand):
    help = "Seed demo doctors, patients, and sample appointments."

    def handle(self, *args, **options):
        # ---- 1. Create Patients ----
        patients_data = [
            {"name": "Alice Chen", "email": "alice@example.com", "phone": "4155550001"},
            {"name": "Bob Lin", "email": "bob@example.com", "phone": "4155550002"},
            {"name": "Cathy Wu", "email": "cathy@example.com", "phone": "4155550003"},
            {"name": "David Lee", "email": "david@example.com", "phone": "4155550004"},
            {"name": "Eric Zhang", "email": "eric@example.com", "phone": "4155550005"},
        ]

        for p in patients_data:
            Patient.objects.get_or_create(name=p["name"], defaults={"email": p["email"], "phone": p["phone"]})

        # ---- 2. Create Doctors ----
        doctors_data = [
            {"name": "Dr. Eva Wang", "specialty": "Cardiology"},
            {"name": "Dr. Mike Zhou", "specialty": "Internal Medicine"},
            {"name": "Dr. Helen Xu", "specialty": "Dermatology"},
            {"name": "Dr. Jason Liu", "specialty": "Pediatrics"},
            {"name": "Dr. Kevin Tang", "specialty": "Neurology"},
        ]

        for d in doctors_data:
            Doctor.objects.get_or_create(name=d["name"], defaults={"specialty": d["specialty"]})

        # ---- 3. Create Appointments ----
        today = date.today()
        patients = list(Patient.objects.all())
        doctors = list(Doctor.objects.all())
        sample_times = [time(9, 0), time(9, 30), time(10, 0), time(10, 30), time(11, 0)]

        count = 0
        for i, patient in enumerate(patients[:5]):
            doctor = doctors[i % len(doctors)]
            appt_date = today + timedelta(days=i % 2)   # 今天或明天
            appt_time = sample_times[i % len(sample_times)]
            Appointment.objects.get_or_create(
                patient=patient,
                doctor=doctor,
                appointment_date=appt_date,
                appointment_time=appt_time,
                defaults={"reason": "Routine check-up"},
            )
            count += 1

        self.stdout.write(self.style.SUCCESS(f"✅ Seeded {len(patients)} patients, {len(doctors)} doctors, {count} appointments."))
