from rest_framework import generics
from django.contrib.auth.models import User
from core.serializers import RegisterSerializer
from rest_framework.permissions import AllowAny

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]
