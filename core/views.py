from rest_framework import generics, viewsets, permissions
from .models import Patient, Doctor, PatientDoctorMapping
from django.contrib.auth.models import User
from .serializers import RegisterSerializer, PatientSerializer, DoctorSerializer, PatientDoctorMappingSerializer
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.decorators import action

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

class PatientViewSet(viewsets.ModelViewSet):
    serializer_class = PatientSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Patient.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [permissions.IsAuthenticated]  # All actions require auth


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