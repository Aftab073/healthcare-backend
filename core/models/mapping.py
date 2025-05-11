from django.db import models
from .patient import Patient
from .doctor import Doctor

class PatientDoctorMapping(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='mappings')
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='mappings')
    assigned_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.patient.name} → {self.doctor.name}"
