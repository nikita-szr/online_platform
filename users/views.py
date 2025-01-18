from rest_framework import viewsets, permissions
from .permissions import IsModerator
from .models import CustomUser, Payment
from .serializers import (
    UserSerializer,
    UserProfileSerializer,
    PaymentSerializer,
    UserRegistrationSerializer,
)
from users.services import create_stripe_price, create_stripe_sessions, create_stripe_product


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

    def perform_create(self, serializer):
        payment = serializer.save(user=self.request.user)
        product_id = create_stripe_product(payment)
        price = create_stripe_price(payment.amount, product_id)
        session_id, payment_link = create_stripe_sessions(price)
        payment.session_id = session_id
        payment.link_to_payment = payment_link
        payment.save()


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
