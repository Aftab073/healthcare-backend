from rest_framework import serializers
from core.models import PatientDoctorMapping

class PatientDoctorMappingSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientDoctorMapping
        fields = '__all__'

    def validate(self, data):
        patient = data.get('patient')
        doctor = data.get('doctor')
        if PatientDoctorMapping.objects.filter(patient=patient, doctor=doctor).exists():
            raise serializers.ValidationError("This doctor is already assigned to this patient.")
        return data
