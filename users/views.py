from rest_framework import viewsets, permissions
from .permissions import IsModerator
from .models import CustomUser, Payment
from .serializers import (
    UserSerializer,
    UserProfileSerializer,
    PaymentSerializer,
    UserRegistrationSerializer,
)


class UserViewSet(viewsets.ModelViewSet):
    """viewset for users"""
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return CustomUser.objects.all()
        return CustomUser.objects.filter(id=user.id)

    def perform_create(self, serializer):
        serializer.save()


class PaymentViewSet(viewsets.ModelViewSet):
    """viewset for payments"""
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [permissions.IsAuthenticated, IsModerator]

    def get_queryset(self):
        return Payment.objects.all()


class UserProfileView(viewsets.GenericViewSet):
    """viewset for userprofile"""
    queryset = CustomUser.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user


class UserRegistrationViewSet(viewsets.ModelViewSet):
    """viewset for users registration"""
    queryset = CustomUser.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [permissions.AllowAny]
