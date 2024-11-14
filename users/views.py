from django.shortcuts import render

from rest_framework import generics
from .models import CustomUser
from .serializers import UserProfileSerializer
from rest_framework.permissions import IsAuthenticated

class UserProfileView(generics.RetrieveUpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user
