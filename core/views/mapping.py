from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from core.models import PatientDoctorMapping
from core.serializers import PatientDoctorMappingSerializer

class MappingViewSet(viewsets.ModelViewSet):
    serializer_class = PatientDoctorMappingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return PatientDoctorMapping.objects.all()

    @action(detail=True, methods=['get'])
    def patient(self, request, pk=None):
        mappings = PatientDoctorMapping.objects.filter(patient_id=pk)
        serializer = self.get_serializer(mappings, many=True)
        return Response(serializer.data)
