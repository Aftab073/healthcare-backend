from rest_framework import viewsets, permissions
from core.models import Doctor
from core.serializers import DoctorSerializer

class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [permissions.IsAuthenticated]
